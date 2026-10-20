from picola import PiCola
from typing import TypeVar, Optional, Generic

T = TypeVar("T")

class _Nodo(Generic[T]):

    __slots__ = ("elemento", "siguiente")

    def __init__(self, elemento : T) -> None:
        self.elemento : T = elemento
        self.siguiente : Optional[_Nodo[T]] = None

class Pila(PiCola[T]):

    def __init__(self) -> None:
        self.__tope : Optional[_Nodo[T]] = None
        self.__tamanio = 0

    def meter(self, elemento : T) -> None:
        pass

    def sacar(self) -> T:
        pass
    
    def mira(self) -> T:
        pass

    def esta_vacia(self) -> bool:
        pass

    def devolver_tamanio(self) -> int:
        pass

    def __eq__(self, otro: object) -> bool:
        pass

    def __str__(self) -> str:
       pass