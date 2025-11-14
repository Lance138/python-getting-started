from typing import Self


class Car:
    def __init__(self, brand: str, horsepower: int) -> None:
        self.brand = brand
        self.horsepower = horsepower

    def __str__(self) -> str:  # Dundermethod example
        return f'{self.brand}, {self.horsepower}hp'

    def __add__(self, other: Self) -> str:
        return f'{self.brand}& {other.brand}'


volvo: Car = Car("Volvo ", 200)
bmw: Car = Car('BMW', 300)
print(volvo + bmw)
