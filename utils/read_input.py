from typing import Type, TypeVar

T = TypeVar("T")

def read_input(file_name : str, cast : Type[T] = str) -> list[T]:
    return [cast(line.strip()) for line in open(file_name, 'r').readlines()]

def read_chars(file_name : str, cast : Type[T]) -> list[list[T]]:
    return [[cast(char) for char in line.strip()] for line in open(file_name, 'r').readlines()]