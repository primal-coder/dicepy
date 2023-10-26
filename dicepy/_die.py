from time import sleep as _sleep
from random import choice as _choice, randint as _randint
import types as _types
from typing import Union as _Union
import pyglet as _pyglet

class MetaDie(type):
    def __new__(cls, name, bases, attrs):
        attrs['_dispatcher'] = _pyglet.event.EventDispatcher()
        if name == 'Die':
            attrs['_dispatcher'].register_event_type('on_roll')
            attrs['_dispatcher'].register_event_type('on_rolls')
        elif name == 'd20':
            attrs['_dispatcher'].register_event_type('on_check')
        return super().__new__(cls, name, bases, attrs)
        
class Die(metaclass=MetaDie):
    """
    ~py class:: Die(value=6)
    ~_pyglet::event::EventDispatcher

    A class to represent a die, which can be rolled to produce a random value between 1 and the specified number of
    sides, or flipped like a coin to produce either "heads" or "tails". Die objects can be used as arguments to the
    roll function. The roll function will return the result of the roll. The roll function can also be used to roll
    multiple die at once, and will return the total of all die rolled. The roll function can also be used to roll a
    sequence of die and will return a tuple of the results of the rolls. The roll function can also be used to roll
    ability scores and will return a list of 6 ability scores ordered from highest to lowest. The Die class subclasses
    the _pyglet.event.EventDispatcher class and raises an event "on_roll" when the die is rolled. The Die class also
    raises an event "on_rolls" when the roll function is used to roll a sequence of die.

    Attributes:
    value (int): The number of sides on the die. Defaults to 6 if no value is specified.

    Methods:
    roll(self) -> int:
    Rolls the die and returns a random value between 1 and the number of sides on the die.
    Raises an event "on_roll" with the last roll as argument.

    rolls(self) -> tuple:
    Rolls the die and returns a tuple of the results of the rolls.

    flip(self) -> str:
    Flips the coin and returns either "heads" or "tails".

    __str__(self) -> str:
    Returns a string representation of the die.

    __repr__(self) -> str:
    Returns a string representation of the die.

    __int__(self) -> int:
    Returns the number of sides on the die.

    Events:
    on_roll(self, roll: int):
    Event raised when the die is rolled.

    on_rolls(self, rolls: tuple):
    Event raised when the die is rolled multiple times.

    """
    def __init__(
            self,
            value: int = None
    ) -> None:
        super().__init__()
        self.value = value if value is not None else 6
        if self.value > 2:  # if the die is not a coin
            def roll(self) -> int:
                """
                Rolls the die and returns a random value between 1 and the number of sides on the die.
                Raises an event "on_roll" with the last roll as argument.

                @param self:
                @return:
                """
                self.last_roll = _randint(1, self.value)
                self._dispatcher.dispatch_event('on_roll', self.last_roll)
                _sleep(_choice([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]))
                return self.last_roll

            setattr(self, 'roll', _types.MethodType(roll, self))
            setattr(self, 'last_roll', None)

            def rolls(self, quantity: int = None, total: bool = False) -> _Union[tuple, int]:
                """
                Rolls the die a specified number of times (defaulting to 1) and returns a tuple of the results. If the
                total argument is True, the sum of the rolls is returned instead of the tuple. Raises an event "on_rolls"
                with the last roll as argument.

                @param self:
                @param quantity:
                @param total:
                """

                r = []
                for _ in range(quantity):
                    r.append(_randint(1, self.value))
                self.last_roll = sum(r) if total else tuple(r)
                self._dispatcher.dispatch_event('on_rolls', self.last_roll)
                return self.last_roll

            setattr(self, 'rolls', _types.MethodType(rolls, self))
        else:  # if the die is a coin
            def flip(self) -> str:
                """
                Flips the die like a coin and returns either "heads" or "tails".
                Raises an event "on_roll" with the last flip as argument.

                @param self:
                @return:
                """

                flip = _randint(0, 1)
                sides = ['heads', 'tails']
                self.last_flip = sides[flip]
                self._dispatcher.dispatch_event('on_roll', self.last_flip)
                return self.last_flip

            setattr(self, 'flip', _types.MethodType(flip, self))
            setattr(self, 'last_flip', None)

            
    def __str__(self):
        return f'd{self.value}' if self.value > 2 else 'coin'

    def __repr__(self):
        return f'{self.value}-sided die' if self.value > 2 else 'coin'

    def __int__(self):
        return self.value
    
class d20(Die):
    """
    A class to represent a d20, which can be rolled to produce a random value between 1 and 20. The class also has a
    check function which accepts an ability_modifier and dc as arguments. The class also has a get_last_check function
    which returns the result of the last check. The class also has an on_check event which is raised when a check is
    made. The event passes the result of the check as an argument.

    Attributes:
    value (int): The number of sides on the die. Defaults to 20 if no value is specified.

    Methods:
    check(self, mod: int, dc: int) -> None:

    get_last_check(self) -> bool:
    """

    def __init__(self):
        super(d20, self).__init__(20)
        self._last_check_val = None
        self._last_check_bool = None
        self._last_check = None

    @property
    def last_check(self):
        return self._last_check        

    @last_check.setter
    def last_check(self, value):
        self._last_check_val = value[0]
        self._last_check_bool = value[1]
        self._last_check = value
    
    @property
    def last_check_val(self):
        return self._last_check_val
    
    @property
    def last_check_bool(self):
        return self._last_check_bool
        
    def check(self, mod: int = None, dc: int = None) -> bool:
        """
        Rolls the die and checks if the result plus the modifier is greater than or equal to the dc. Raises an event

        @param mod:
        @param dc:
        @return:
        """
        res = self.roll()
        fin = res + mod
        self.last_check = (fin, fin >= dc)
        self._dispatcher.dispatch_event('on_check', self.last_check)
        return self.last_check

    def get_last_check(self, val: bool = False) -> _Union[bool, int]:
        """
        Returns the result of the last check.
        @return:
        """
        return self.last_check_val if val else self.last_check_bool