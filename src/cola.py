from picola import PiCola
from typing import TypeVar, Optional,Generic

T = TypeVar("T")

class _Nodo(Generic[T]):

    __slots__ = ("elemento", "siguiente")

    
class Cola(PiCola[T]):

    