# TODO Написать 3 класса с документацией и аннотацией типов
class Stone:
    def __init__(self, weight: float, volume: float):
        """
                Создание и подготовка к работе объекта "Камень"
                :param weight: Масса камня
                :param volume: Объем камня
                Примеры:

                >>> stone = Stone(500, 0)  # инициализация экземпляра класса
        """
        self.init_weight(weight)
        self.init_volume(volume)

    def init_weight(self, weight: float):
            if not isinstance(weight, (int, float)):
                raise TypeError("Камень всегда материальный, а значит его масса описывается типами int или float ")
            if weight < 0:
                raise ValueError("Масса камня должна быть положительной")
            self.weight = weight

    def init_volume(self, volume: float):
            if not isinstance(volume, (int, float)):
                raise TypeError("Камень всегда материальный, а значит его объем описывается типами int или float ")
            if volume < 0:
                raise ValueError("Масса камня должна быть положительной")
            self.volume = volume
    def stone_density (self) ->float:
        """
            Функция определения пределение плотности камня
    
            :return: возвращает плотность камня
            Пример:
            >>> stone = Stone(5,0.00001)
            >>> stone_dest = stone.stone_density()
        """

    def stone_separation(self, ratio: float):
        """
            Функция разделения камня на две части

            :param ratio: Доля массы или объема одной из частей разделенного камня от изначального
            :raise ValueError: Если доля больше 1 или меньше нуля, то выдаем ошибку
            :return: возвращает массу и объем запрашиваемой доли камня камня
            Пример:
            >>> stone = Stone(5,0.00001)
            >>> stone.stone_separation(0.5)
        """


class Knife:
    def __init__(self, blade_material: str, handle_material: str, blade_lenght: float):
        """
                Создание и подготовка к работе объекта "Нож"
                :param blade_material: Материал лезвия
                :param handle_material: Материал рукоятки
                :param blade_lenght: Длина лезвия в миллиметрах
                Примеры:

                >>> knife = Knife("Steel", "Plastic", 30)  # инициализация экземпляра класса
        """
        self.init_blade_material(blade_material)
        self.init_handle_material(handle_material)
        self.init_blade_lenght(blade_lenght)

    def init_blade_material(self, blade_material: str):
        if not isinstance(blade_material, str):
            raise TypeError("Материал лезвия описывается строкой(str)")
        self.blade_material = blade_material

    def init_handle_material(self, handle_material: str):
        if not isinstance(handle_material, str):
            raise TypeError("Материал рукоятки описывается строкой(str)")
        self.handle_material = handle_material

    def init_blade_lenght(self, blade_lenght: float):
            if not isinstance(blade_lenght, (int, float)):
                raise TypeError("Длина лезвия описывается типами int или float ")
            if blade_lenght < 0:
                raise ValueError("Длина лезвия должна быть положительной")
            self.blade_lenght = blade_lenght

    def is_it_steel_knife(self) -> bool:
        """
            Проверяет является ли нож стальным

            :return: является ли нож стальным
            Пример:
            >>> knife = Knife("Steel","Plastic", 30)
            >>> knife.is_it_steel_knife()
        """

    def knife_type(self) ->str:
        """
            Функция определяет назначение ножа в зависимости от его длины и материала

            :return: возвращает строку с назначением ножа
            Пример:
            >>> knife = Knife("Steel","Plastic", 30)
            >>> knife.knife_type()
        """

class Tea:
    def __init__(self, manufacturer: str, varieties: str, bags_number: int, bag_weight: float):
        """
                Создание и подготовка к работе объекта "Чай"
                :param manufacturer: Производитель чая
                :param varieties: Сорт чая
                :param bags_number: Количество пакетиков в упаковке
                :param bag_weight: Масса чая в пакетике в граммах
                Примеры:

                >>> tea = Tea("Tess", "Green", 30, 2)  # инициализация экземпляра класса
        """
        self.init_manufacturer(manufacturer)
        self.init_varieties(varieties)
        self.init_bags_number(bags_number)
        self.init_bag_weight(bag_weight)

    def init_manufacturer(self, manufacturer: str):
            if not isinstance(manufacturer, str):
                raise TypeError("Название производителя описывается в виде строки")
            self.manufacturer = manufacturer

    def init_varieties(self, varieties: str):
        if not isinstance(varieties, str):
            raise TypeError("Название сорта описывается в виде строки")
        self.varieties = varieties

    def init_bags_number(self, bags_number: int):
            if not isinstance(bags_number, int):
                raise TypeError("Количество пакетиков чая может быть только целым")
            if bags_number < 0:
                raise ValueError("Количество пакетиков чая может быть только положительным")
            self.bags_number = bags_number

    def init_bag_weight(self, bag_weight: float):
        if not isinstance(bag_weight, (int,float)):
            raise TypeError("Вес чая в пакетике описывается только типами int и float")
        if bag_weight < 0:
            raise ValueError("Вес чая в пакетике может быть только положительным")
        self.bag_weight = bag_weight

    def teatime(self)->None:
        """
            Время пить чай, уменьшает количество пакетиков в пачке на 1

            :raise ValueError: Если чая не осталось, то выдаем ошибку

            Пример:
            >>> tea = Tea("Tess", "Green", 30, 2)
            >>> tea.teatime()
        """

    def sumweight(self)->float:
        """
            Определяет суммарную массу чая, который остался

            :return: Масса чая
        """

if __name__ == "__main__":
    doctest.testmod()
    pass
