import gym
import numpy as np

from ppo import PPOAgent


def main():
    env = gym.make('CarRacing-v2', continuous=False)

    N = 2
    batch_size = 2
    n_epochs = 10
    learning_rate = 0.02
    dimensions = int(np.prod(env.observation_space.shape))

    agent = PPOAgent(n_actions=env.action_space.n, batch_size=batch_size, n_epochs=n_epochs, lr=learning_rate, 
    input_dims=dimensions)

    n_games = 500

    learn_iters = 0
    avg_score = 0
    best_score = env.reward_range[0]
    score_history = []
    n_steps = 0
    print("Starting training...")
    for ep in range(n_games):
        obs = env.reset()[0].reshape(dimensions) / 255
        done = False
        score = 0
        while not done:
            action, prob, val = agent.choose_action(obs)
            obs_, reward, done, info, data = env.step(action)
            n_steps += 1
            score += reward
            agent.save_state(obs, action, prob, val, reward, done)

            if learn_iters % N == 0:
                agent.learn()
                learn_iters += 1
            obs = obs_.reshape(dimensions) / 255

        score_history.append(score)
        avg_score = np.mean(score_history[-100:])

        if avg_score > best_score:
            best_score = avg_score
            agent.save_model()

        print('episode: ', ep, 'score: %.1f' % score, 'avg score %.1f' % avg_score, 'best score %.1f' % best_score, 'steps', n_steps)

if __name__ == '__main__':
    main()