from random import randint as _randint
from typing import Union as _Union, Optional as _Optional, Callable as _Callable

from ._die import Die as _Die

# Create a static roll function which accepts the die to roll as an argument.

# The function should return the result of the roll.

def roll(
        die: _Union[_Callable[[int], None], int, tuple[_Callable, ], tuple[int, ], list[_Callable, ], list[int, ]] = None
) -> int:
    """
    Rolls a die with the specified number of sides.

    Args: die (_Union[_Callable[[int], None], int]): The die to roll. Either an integer representing the number of
    sides on a standard die, a custom die object with a 'roll' method that takes an integer argument and returns an
    integer, or None.

    Returns:
        int: The result of the die roll.
    """
    if die is not None:
        if isinstance(
                die,
                _Die
        ):
            return die.roll()
        elif isinstance(die, int):
            d = _Die(die)
            return d.roll()
        elif isinstance(die, (tuple, list)):
            raise ValueError(
                "Try using the rolls function instead of the roll function for rolling multiple die."
                "\nLike this:\n\t`rolls(3, d6)`")
        else:
            try:
                i = int(die)
                d = Die(i)
                return d.roll()
            except ValueError as e:
                raise ValueError(
                    "Try again with an argument that can be interpreted as an integer or one as an instance of the "
                    "Die class."
                    "\nLike this:\n\t`roll(6)` or `roll(d8)`"
                ) from e
    else:
        standard = Die(6)
        return standard.roll()


# Create a static rolls function which accepts a number of die to roll and the type of die to roll.

# The function should return the total of all die rolled.

def rolls(
        dice: _Optional[int] = None,
        die: _Union[_Callable[[int], None], int] = None
) -> int:
    """
    Rolls a number(dice) of die(die) and returns the total. If no arguments are provided, a single 6-sided die is rolled.


    @param dice:
    @param die:
    @return:
    """
    if dice is None:
        dice = 1
    if die is None:
        die = 6
    if isinstance(
        die,
        Die
    ):
        return sum(die.roll() for _ in range(dice))
    elif isinstance(
        die,
        int
    ):
        d = _Die(die)
        return sum(d.roll() for _ in range(dice))

# Create static roll_sequence function which accepts the number of die to roll and the type of die to roll.

# This function should return a set of `die.roll()` results at the length of the value of the `die` parameter


def roll_sequence(
        dice: int,
        die: _Union[_Callable[[int], None], int]
) -> tuple:
    """
    Rolls a sequence of die and returns the results as a tuple.

    @param dice:
    @param die:
    @return:
    """
    result = [die.roll() for _ in range(dice)]
    return tuple(result)


# Create a static ability_roll function which accepts no arguments

# The function should return a tuple of 4 numbers as a list, each between 1 and 6, and the sum of the 3 highest numbers.

def ability_roll() -> tuple:
    """
    Rolls 5d6 and returns the sum of the 3 highest numbers.

    @return:
    """
    from ._dice import d6
    rs = [d6.roll() for _ in range(5)]
    rs.sort()
    return rs, sum(rs[2:])


# Create a static ability_rolls function which accepts no arguments

# The function should return a list of all 6 ability rolls ordered from highest to lowest.

def ability_rolls(expunge: _Optional[bool] = True) -> list:
    """
    Rolls 6 ability scores and returns them in a list ordered from highest to lowest.

    @return:
    """
    rs = [ability_roll() for _ in range(6)]
    rs = [rs[i][1] for i in range(len(rs))]
    rs.sort(reverse=True)
    if expunge and rs[-1] < 12:
        print("Expunging low ability scores (<= 11) ... ")
        rs = ability_rolls()
    return rs


# Create a check function which accepts an ability_modifier and dc as arguments.

# The function should return True if the ability_modifier is greater than or equal to the dc.

# The function should return (True, True) if the result of the roll is a 20 to indicate a critical success.

# The function should return False if the ability_modifier is less than the dc or the result of the roll is a 1.

def check(
        modifier: _Optional[int] = None,
        dc: _Optional[int] = None) -> bool:
    from ._dice import d20
    mod = modifier if modifier is not None else 0
    return d20.check(mod, dc)
