from decimal import Decimal
from typing import Sequence

"""
The coin change problem is a discrete combinatorial optimization problem equivalent to the unbounded knapsack problem.
"""


def money_0(sorted_arr_dec: Sequence[Decimal], total: Decimal) -> tuple[list[int], Decimal]:
    """
    brute force version, low efficiency.
    """
    counts = [0 for _ in range(len(sorted_arr_dec))]

    for i in range(len(sorted_arr_dec)):
        while total >= sorted_arr_dec[i]:
            counts[i] += 1
            total -= sorted_arr_dec[i]

    return counts, total


def money_1(sorted_arr_dec: Sequence[Decimal], total: Decimal) -> tuple[list[int], Decimal]:
    """
    mod, div version, recommend
    """
    counts = [0 for _ in range(len(sorted_arr_dec))]

    for i in range(len(sorted_arr_dec)):
        counts[i] = int(total // sorted_arr_dec[i])
        total %= sorted_arr_dec[i]

    return counts, total


if __name__ == '__main__':
    arr_ = [
        Decimal("100"),
        Decimal("50"),
        Decimal("20"),
        Decimal("10"),
        Decimal("5"),
        Decimal("1"),
        Decimal("0.5"),
        Decimal("0.1"),
        Decimal("0.01")
    ]

    total_1 = Decimal("3.9")
    total_2 = Decimal("17892.89")

    print(money_1(sorted_arr_dec=arr_, total=total_1))
    print(money_1(sorted_arr_dec=arr_, total=total_2))
