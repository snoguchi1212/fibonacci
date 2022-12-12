from dataclasses import dataclass, field, InitVar
from typing import TypeAlias

Sequence: TypeAlias = tuple[int]


@dataclass
class FibonacciNumber:

    sequence: Sequence = field(init=False)
    sequence_length: InitVar[int] = 0

    def __post_init__(self, sequence_length) -> None:
        _sequence: list[int] = []
        for i in range(1, sequence_length + 1):
            if i == 1:
                _sequence = [1]
            elif i == 2:
                _sequence = [1, 1]
            else:
                next_num = _sequence[-1] + _sequence[-2]
                _sequence += [next_num]

        self.sequence = tuple(_sequence)

    def fibonacci_nth_number(self) -> int:
        return self.sequence[-1]
