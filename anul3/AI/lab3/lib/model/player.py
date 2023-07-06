
class Player:
    def __init__(self, playerIndex: int, names: str, directions: list, matrix: list):
        self.__playerName = names[playerIndex]
        self.__strategies = directions[playerIndex*2:(playerIndex*2)+2]
        self.__payoffs = [[0, 0],[0, 0]]
        self.__best_strategy = []
        self.__id = playerIndex
        
        for line in range(len(matrix)):
            for col in range(len(matrix[line])):
                self.__payoffs[line][col] = int(matrix[line][col].split('/')[playerIndex])
    @property
    def payoffs(self):
        return self.__payoffs

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__playerName
    
    @property
    def strategies(self):
        return self.__strategies

    @property
    def best_strategy(self):
        return self.__best_strategy

    def set_best_strategy(self, best_strat):
        self.__best_strategy = best_strat