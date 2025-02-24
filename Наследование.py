class Animal:
    """
    Базовый класс для всех животных.
    """

    def __init__(self, name: str, age: int) -> None:
        """
        Инициализация животного.

        :param name: Имя животного.
        :param age: Возраст животного.
        """
        self.__name = name  # Непубличный атрибут
        self.__age = age    # Непубличный атрибут

    def speak(self) -> str:
        """
        Метод, который возвращает звук, издаваемый животным.
        По умолчанию возвращает 'Some sound'.
        """
        return 'Some sound'

    def __str__(self) -> str:
        """
        Возвращает строковое представление животного.
        """
        return f"Animal(name={self.__name}, age={self.__age})"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление животного.
        """
        return f"Animal('{self.__name}', {self.__age})"
class Dog(Animal):
    """
    Класс для собак, наследуется от Animal.
    """

    def __init__(self, name: str, age: int, breed: str) -> None:
        """
        Инициализация собаки.

        :param name: Имя собаки.
        :param age: Возраст собаки.
        :param breed: Порода собаки.
        """
        super().__init__(name, age)  # Вызов конструктора базового класса
        self.__breed = breed  # Непубличный атрибут

    def speak(self) -> str:
        """
        Переопределение метода speak для собаки.
        Возвращает звук, издаваемый собакой.

        :return: Звук собаки.
        """
        return 'Woof!'

    def __str__(self) -> str:
        """
        Возвращает строковое представление собаки.
        """
        return f"Dog(name={self._Animal__name}, age={self._Animal__age}, breed={self.__breed})"

    def fetch(self, item: str) -> str:
        """
        Метод, который имитирует, что собака приносит предмет.

        :param item: Предмет, который собака должна принести.
        :return: Сообщение о том, что собака принесла предмет.
        """
        return f"{self._Animal__name} fetched the {item}!"
class Cat(Animal):
    """
    Класс для кошек, наследуется от Animal.
    """

    def __init__(self, name: str, age: int, color: str) -> None:
        """
        Инициализация кошки.

        :param name: Имя кошки.
        :param age: Возраст кошки.
        :param color: Цвет кошки.
        """
        super().__init__(name, age)  # Вызов конструктора базового класса
        self.__color = color  # Непубличный атрибут

    def speak(self) -> str:
        """
        Переопределение метода speak для кошки.
        Возвращает звук, издаваемый кошкой.

        :return: Звук кошки.
        """
        return 'Meow!'

    def __str__(self) -> str:
        """
        Возвращает строковое представление кошки.
        """
        return f"Cat(name={self._Animal__name}, age={self._Animal__age}, color={self.__color})"

    def climb(self) -> str:
        """
        Метод, который имитирует, что кошка лезет на дерево.

        :return: Сообщение о том, что кошка залезла на дерево.
        """
        return f"{self._Animal__name} climbed a tree!"