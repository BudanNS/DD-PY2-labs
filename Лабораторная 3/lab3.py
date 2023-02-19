class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def set_name(self, new_name: str):
        self._name = new_name

    def set_author(self, new_author: str):
        self._author = new_author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.init_pages(pages)

    def init_pages(self, pages: int):
        if not isinstance(pages, int):
            raise TypeError("Pages must be int ")
        if pages <= 0:
            raise ValueError("Pages must be positive")
        self.pages = pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self.pages})"

class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.init_duration(duration)

    def init_duration(self, duration: float):
        if not isinstance(duration, float):
            raise TypeError("Duration must be float ")
        if duration <= 0:
            raise ValueError("Duration must be positive")
        self.duration = duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self.duration})"
