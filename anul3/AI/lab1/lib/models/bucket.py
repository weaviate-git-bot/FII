class Bucket:
    def __init__(self, max_capacity: int, litters_filled: int = 0):
        self.__liters_filled = litters_filled
        self.__max_capacity = max_capacity

    def __str__(self):
        return f"Bucket( liters_filled = {self.__liters_filled}, max_capacity = {self.__max_capacity} )"

    @property
    def current_filled_litters(self) -> int:
        return self.__liters_filled

    @property
    def max_capacity(self) -> int:
        return self.__max_capacity

    def pour(self, amount: int) -> None:
        self.__liters_filled = amount if amount <= self.__max_capacity else self.__max_capacity
        self.__liters_filled = amount if amount >= 0 else 0