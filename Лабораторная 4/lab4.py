class Headphones:
    def __init__(self, name: str, producer: str, price: float, iswireless: bool) -> None:
        self.name = name
        self.producer = producer
        self.price = price
        self.iswireless = iswireless

        """
                Создание и подготовка к работе базового класса "Headphones"
                :param name: Название модели наушников
                :param producer: Название производителя
                :param price: Цена наушников
                :param iswireless: Параметр показывающий являются ли наушники безпроводными
                Примеры:

                >>> Headphone1 = Headphones("Airpods 2", "Apple", 1000, 1)  # инициализация экземпляра класса
        """

    def __str__(self)-> str:
        """
            Метод взвращающий название модели наушников
            :return: Возвращает название модели наушников
        """
        return f'Headphone model: {self.name!r}'

    def __repr__(self) -> str:
        """
                    Метод взвращающий подробную информацию о модели наушников
                    :return: Возвращает подробную информацию модели наушников
                """
        return f'Headphone(model={self.name!r}, producer={self.producer!r}, price={self.price})'

    def newprice(self, newprice: int) -> None:
        """
        Метод изменяющий цену наушников
        :param newprice: Новая цена наушников
        :return: Изменяет цену наушников в классе
        """
        self.price = newprice

    def iswireless(self) -> str:
        """
        Метод вовзращающий информацию о том, являются ли наушники беспроводными
        :return: В зависимости от информации о наушниках выводит на экран информацию являются наушники проводными или беспроводными
        """
        if self.iswireless:
            return f'This Headphones is wireless'
        else:
            return f'This Headphones is wired'

class Earphones(Headphones):
    def __init__(self,name: str, producer: str, price: float,iswireless: bool,  types="Earphones"):
        """

        Создание и подготовка к работе базового класса "Earphones"
        :param name: Название модели наушников
        :param producer: Название производителя
        :param price: Цена наушников
        :param iswireless: Параметр показывающий являются ли наушники безпроводными
        :param types: Объект в котором хранится тип наушников, по умолчанию "Earphones"
        """
        super().__init__(name, producer, price, iswireless)
        self.types = types

    def __str__(self) -> str:
        """
            Метод взвращающий название модели наушников
            :return: Возвращает название модели наушников
        """
        return f'{self.types} model: "{self.name!r}"'

    def __repr__(self) -> str:
        """
            Метод взвращающий подробную информацию о модели наушников
            :return: Возвращает подробную информацию модели наушников
        """
        return f'{self.types}(model={self.name!r}, producer={self.producer!r}, price={self.price})'

    def newprice(self, newprice: int) -> None:
        """
            Метод изменяющий цену наушников
            :param newprice: Новая цена наушников
            :return: Изменяет цену наушников в классе
        """
        super().newprice(newprice)

if __name__ == "__main__":

    pass
