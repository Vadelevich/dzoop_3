class Flight:

    def __init__(self, city_from, city_to):
        self.__city_from = city_from
        self.__city_to = city_to

    def __str__(self):
        return f'{self.__class__.__name__} from {self.__city_from} to {self.__city_to}'





print(Flight(input(), input()))
# Ввод
# АВС
# CDE
# Вывод
# Flight from АВС to CDE