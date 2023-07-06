from lib.model import Player

class DominantStrategyAlgorithm:
    def __init__(self, p1: Player, p2: Player):
        self.__p1 = p1
        self.__p2 = p2

    def run(self):
        print("Running dominant strategy algorithm")
        self.__print_dominant_strategy(self.__p1, self.__p2)
        self.__print_dominant_strategy(self.__p2, self.__p1)

    def __print_dominant_strategy(self, player1: Player, player2: Player):
        print("-="*10, end=' ')
        print(f"Best strategy for player {player1.name}", end=' ')
        print("=-"*10)

        dom_strategy = self.__get_dominant_strategy(player1, player2)
        player1.set_best_strategy(dom_strategy)
        best_strategies = list()
        for idx in range(len(player2.strategies)):
            for strategy in dom_strategy[idx]:
                best_strategies.append(player1.strategies[strategy[player1.id]])

            print(f"If player {player2.name} plays {player2.strategies[idx]}, then {player1.name} response is {set(best_strategies)}")

        print()
        if len(best_strategies) <= 0:
            print("No dominant strategy found")
            return

        print(f"Best strategy for player {player1.name} is {max(best_strategies)}")
        print('\n')

    def __get_dominant_strategy(self, player1: Player, player2: Player):
        player_best_strategies = []
        for p2_strategy in range(len(player2.strategies)):
            max_payoff = -1
            current_best_strategy = []
            for p1_strategy in range(len(player1.strategies)):
                current_payoff = player1.payoffs[p1_strategy][p2_strategy]
                if current_payoff > max_payoff:
                    max_payoff = current_payoff
                    current_best_strategy = [[p1_strategy, p2_strategy]]
                elif max_payoff == current_payoff:
                    current_best_strategy.append([p1_strategy, p2_strategy])
            
            player_best_strategies.append(current_best_strategy)
        
        return player_best_strategies