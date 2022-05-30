from typing import List, Dict, Set, Optional, Any, Sequence, Tuple, Callable, Type
from typing import TypeVar # Generics


s: Set[int] = {1,2,3,4}
l: List[int] = [1,2,3,4]
d: Dict[int, str] = {1:'1', 2:'2'}

Vector = List[float]   # Custom type (typedef in other languages such as dart)
Vectors = List[Vector]

v: Vector = [1., 2., 3.]
m: Vectors = [[1., 2.], [3., 4.]]


def f(a:Optional[int] = 0):
    print(a)

def f2(b:Sequence[Any]):  # Sequence of Any type
    print(b, '{can be tuple, list,...}')

t: Tuple[int, int, int] = [1,2,3]  # For every single param

def adder(x: int, y: int=1)->int:
    return x + y

def f3(c: Callable[[int, Optional[int]],int])->int:
    return c(1)

f3(adder)

def squarer():
    func: Callable[[int], int] = lambda x: x**2  # For lambda type hints
    return func

T  = TypeVar('T')  # Generics
def f4(l: List[T], idx: int) -> T:  # Genrics Type 
    return l[idx]

