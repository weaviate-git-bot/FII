class NashEquilibriaAlgorithm:
    def __init__(self, p1, p2):
        self.__p1 = p1
        self.__p2 = p2

    def run(self):
        print("-="*10 + " Nash Equilibria " + "=-"*10)
        if len(self.__p1.best_strategy) <= 0 or len(self.__p2.best_strategy) <= 0:
            print("One or both players don't have a dominant strategy. Nash Equilibria won't run correctly")
        
        equilibrium_payoffs = []
        nash_equilibria = []

        for a_best in self.__p1.best_strategy:
            for b_best in self.__p2.best_strategy:
                for best_strategy in b_best:
                    if best_strategy in a_best:
                        equilibrium_payoffs.append(best_strategy)
                        p1_strat = self.__p1.strategies[best_strategy[self.__p1.id]]
                        p2_strat = self.__p2.strategies[best_strategy[self.__p2.id]]
                        nash_equilibria.append([p1_strat, p2_strat])

        print("We found " + str(len(nash_equilibria)) + " equilibria: " + str(nash_equilibria))
        print("We found " + str(len(equilibrium_payoffs)) + " equilibrium payoffs: " + str(equilibrium_payoffs))