import numpy as np
import tensorflow as tf
import tensorflow.keras as keras
from tensorflow.keras.optimizers import Adam
import tensorflow_probability as tfp

from .memory import Memory
from .networks import ActorNetwork, CriticNetwork

class Agent:

    def __init__(self, n_actions, input_dims, gamma=0.99, lr=0.0003,
                gae_lambda=0.95, policy_clip=0.2, batch_size=64, 
                n_epochs=10, checkpoint_dir='./models/ppo'):
        
        self.actor = None
        self.critic = None

        self.n_actions = n_actions
        self.input_dims = input_dims
        self.gamma = gamma
        self.lr = lr
        self.gae_lambda = gae_lambda
        self.policy_clip = policy_clip
        self.batch_size = batch_size
        self.n_epochs = n_epochs
        self.checkpoint_dir = checkpoint_dir

        self.__init_networks()
        self.memory = Memory(batch_size)

    def save_state(self, state, action, probs, vals, reward, done):
        self.memory.store_memory(state, action, probs, vals, reward, done)

    def save_model(self):
        print('---'*4, 'Saving model', '---'*4)
        self.actor.save(self.checkpoint_dir + '/actor')
        self.critic.save(self.checkpoint_dir + '/critic')

    def load_model(self):
        self.actor = keras.models.load_model(self.checkpoint_dir + '/actor')
        self.critic = keras.models.load_model(self.checkpoint_dir + '/critic')

    def choose_action(self, state):
        state = tf.convert_to_tensor([state], dtype=tf.float32)
        
        probs = self.actor(state)
        dist = tfp.distributions.Categorical(probs)
        action = dist.sample()
        log_prob = dist.log_prob(action)
        value = self.critic(state)

        action = action.numpy()[0]
        log_prob = log_prob.numpy()[0]
        value = value.numpy()[0]

        return action, log_prob, value

    def learn(self):
        for _ in range(self.n_epochs):
            self.__run_epoch()

    def __run_epoch(self):
        states_m, actions_m, old_probs_m, vals_m, rewards_m, dones_m, batches = self.memory.generate_batches()

        values = vals_m
        advantage = np.zeros(len(rewards_m), dtype=np.float32)

        for t in range(len(rewards_m)):
            discount = 1
            a_t = 0

            for k in range(t, len(rewards_m)-1):
                a_t += discount * (rewards_m[k] + self.gamma * vals_m[k+1] * (1-int(dones_m[k])) - vals_m[k])
                discount *= self.gamma * self.gae_lambda

            advantage[t] = a_t

        for batch in batches:
            # persistent= True -> we can backpropagate twice
            with tf.GradientTape(persistent=True) as tape:
                states = tf.convert_to_tensor(states_m[batch], dtype=tf.float32)
                actions = tf.convert_to_tensor(actions_m[batch], dtype=tf.float32)
                old_probs = tf.convert_to_tensor(old_probs_m[batch], dtype=tf.float32)

                probs = self.actor(states)
                dist = tfp.distributions.Categorical(probs=probs)
                new_probs_m = dist.log_prob(actions)

                critic_val = self.critic(states)
                critic_val = tf.squeeze(critic_val, 1)

                ratio = tf.math.exp(new_probs_m - old_probs)
                
                weighted_probs = ratio * advantage[batch]

                clipped_probs = tf.clip_by_value(ratio, 1-self.policy_clip, 1+self.policy_clip)
                weighted_clipped_probs = clipped_probs * advantage[batch]

                actor_loss = -tf.math.minimum(weighted_probs, weighted_clipped_probs)
                actor_loss = tf.math.reduce_mean(actor_loss)

                returns = advantage[batch] + values[batch]

                critic_loss = keras.losses.MSE(critic_val, returns)
            
            actor_params = self.actor.trainable_variables
            critic_params = self.critic.trainable_variables
            actor_grads = tape.gradient(actor_loss, actor_params)
            critic_grads = tape.gradient(critic_loss, critic_params)

            self.actor.optimizer.apply_gradients(zip(actor_grads, actor_params))
            self.critic.optimizer.apply_gradients(zip(critic_grads, critic_params))

        
        self.memory.clear_memory()


    def __init_networks(self) -> None:
        self.actor = ActorNetwork(self.n_actions, self.input_dims)
        self.critic = CriticNetwork(self.input_dims)

        self.actor.compile(optimizer=Adam(learning_rate=self.lr))
        self.critic.compile(optimizer=Adam(learning_rate=self.lr))