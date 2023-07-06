import matplotlib.pyplot as plt
import numpy as np
from enum import Enum

from typing import List

class State:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __eq__(self, x: 'State') -> bool:
        return self.x == x.x and self.y == x.y
    
class Directions(Enum):
    NONE = 0
    UP = 1
    DOWN = -1
    LEFT = 1
    RIGHT = -1

    def __int__(self) -> int:
        return self.value

class CliffWalking:
    def __init__(self):
        self.shape = (4, 12)
        self._cliff = np.full(self.shape, -1, dtype=np.int32)
        self._q = np.zeros((4, 12, 4), dtype=np.int16)
        self._cliff[3, 1:-1] = -100
        self._cliff[3, -1] = 100

        self._learning_rate = 0.1
        self._discount_factor = 0.5
        self._alpha = 0.5

        self.rewards_per_episode = []

        self._initial_state = State(3, 0)
        self._final_state = State(3, 11)
        self._current_state = self._initial_state

    def __is_terminal_state(self, state: State) -> bool:
        return self._cliff[state.x, state.y] == -1

    def __get_next_action(self, state: State, eps: int) -> State:
            if np.random.random() < eps:
                return np.argmax(self._q[state.x, state.y])
            else:
                return np.random.randint(4)

    def _validate_and_update(self, state, action):
        # here we should validate if the position will be valid
        new_positon_x = state.x + int(action[0])
        new_positon_y = state.y + int(action[1])

        if new_positon_x < 0 or new_positon_x >= self.shape[0]:
            new_positon_x = state.x

        if new_positon_y < 0 or new_positon_y >= self.shape[1]:
            new_positon_y = state.y


        if self._cliff[new_positon_x, new_positon_y] == -100:
            return self._initial_state

        return State(new_positon_x, new_positon_y)

    def update_position(self, eps = 0.1):
        action_list = [
            [Directions.UP, Directions.NONE],
            [Directions.NONE, Directions.LEFT],
            [Directions.DOWN, Directions.NONE],
            [Directions.NONE, Directions.RIGHT],
        ]

        action_idx = self.__get_next_action(self._current_state, eps)
        action = action_list[action_idx]
        new_state = self._validate_and_update(self._current_state, action)

        if not new_state == self._current_state:
            self._current_state = new_state
            return action_idx                

    def train(self, episodes: int = 1000):
        for ep_idx in range(episodes):
            # print(f"Starting episode {ep_idx}")
            total_episode_reward = 0
            self._current_state = self._initial_state

            while self.__is_terminal_state(self._current_state):
                old_state = self._current_state
                action_taken = self.update_position()

                reward = self._cliff[self._current_state.x, self._current_state.y]
                total_episode_reward += reward
                old_q_values = self._q[old_state.x, old_state.y, action_taken]
                
                temp_diff = reward + (self._discount_factor * np.max(self._q[self._current_state.x, self._current_state.y])) - old_q_values
                
                new_q_value = old_q_values + (self._alpha * temp_diff)
                self._q[old_state.x, old_state.y, action_taken] = new_q_value
            self.rewards_per_episode.append(total_episode_reward)
            if ep_idx % 100 == 0:
                print(f"Episode {ep_idx} finished with reward: {total_episode_reward}")
            # print(f"Episode {ep_idx} finished with reward: {total_episode_reward}")

    def plot(self, episodes: int = 1000) -> None:
            plt.plot([i for i in range(episodes)], self.rewards_per_episode)
            plt.xlabel("Episode")
            plt.ylabel("Total reward")
            plt.show() 

cliff = CliffWalking()
episodes = 500
cliff.train(episodes=episodes)
cliff.plot(episodes=episodes)
print(cliff._q)