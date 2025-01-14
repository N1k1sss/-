import doctest
from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, make: str, model: str, year: int):
        """
        Создание и подготовка к работе объекта "Транспортное средство"

        :param make: Производитель транспортного средства
        :param model: Модель транспортного средства
        :param year: Год выпуска транспортного средства

        Примеры:
        >>> vehicle = Vehicle("Toyota", "Camry", 2020)  # инициализация экземпляра класса
        """
        if not isinstance(make, str):
            raise TypeError("Производитель должен быть строкой")
        if not isinstance(model, str):
            raise TypeError("Модель должна быть строкой")
        if not isinstance(year, int) or year < 1886:  # Первый автомобиль был создан в 1886
            raise ValueError("Год выпуска должен быть целым числом и не меньше 1886")

        self.make = make
        self.model = model
        self.year = year

    @abstractmethod
    def start_engine(self) -> None:
        """
        Запуск двигателя транспортного средства.
        """
        ...

    @abstractmethod
    def stop_engine(self) -> None:
        """
        Остановка двигателя транспортного средства.
        """
        ...


class Computer(ABC):
    def __init__(self, brand: str, ram_size: int, storage_size: int):
        """
        Создание и подготовка к работе объекта "Компьютер"

        :param brand: Бренд компьютера
        :param ram_size: Объем оперативной памяти в ГБ
        :param storage_size: Объем хранилища в ГБ

        Примеры:
        >>> computer = Computer("Apple", 16, 512)  # инициализация экземпляра класса
        """
        if not isinstance(brand, str):
            raise TypeError("Бренд должен быть строкой")
        if not isinstance(ram_size, int) or ram_size <= 0:
            raise ValueError("Объем оперативной памяти должен быть положительным целым числом")
        if not isinstance(storage_size, int) or storage_size <= 0:
            raise ValueError("Объем хранилища должен быть положительным целым числом")

        self.brand = brand
        self.ram_size = ram_size
        self.storage_size = storage_size

    @abstractmethod
    def power_on(self) -> None:
        """
        Включение компьютера.
        """
        ...

    @abstractmethod
    def power_off(self) -> None:
        """
        Выключение компьютера.
        """
        ...


class Book(ABC):
    def __init__(self, title: str, author: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга"

        :param title: Название книги
        :param author: Автор книги
        :param pages: Количество страниц в книге

        Примеры:
        >>> book = Book("1984", "George Orwell", 328)  # инициализация экземпляра класса
        """
        if not isinstance(title, str):
            raise TypeError("Название должно быть строкой")
        if not isinstance(author, str):
            raise TypeError("Автор должен быть строкой")
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом")

        self.title = title
        self.author = author
        self.pages = pages

    @abstractmethod
    def read(self) -> None:
        """
        Чтение книги.
        """
        ...

    @abstractmethod
    def bookmark_page(self, page: int) -> None:
        """
        Установка закладки на странице.

        :param page: Номер страницы для закладки
        """
        ...

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
