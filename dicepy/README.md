# dicepy

Dicepy is composed of three submodules: 'Dice', 'Die' and 'Roll'. 

## Dice

The Dice submodule contains the DiceSet class, which is used to create a set of dice. The DiceSet class instantiates Die objects and provides access to them and their methods through the DiceSet object. A standard set of dice is comprised of a d4, d6, d8, d10, d12, d20 and one coin.

### DiceSet

The DiceSet class is used to create a set of dice. The DiceSet class has the following attributes:

* d4
* d6
* d8
* d10
* d12
* d20
* coin

#### Usage(DiceSet)

```python
from dicepy import Dice

main_set = Dice.DiceSet()
main_set.d20.roll()
```

## Die(submodule)

The Die submodule contains the Die class, which is used to create a single die. The Die class provides methods for rolling the die and accessing the result of the roll. The Die class is not intended to be used directly, but rather through the DiceSet class. The Die submodule also contains the d20 class, which is a subclass of Die and is used to create a d20. The d20 class implements a special roll method called check, which accepts a modifier(mod) and difficulty class(dc) as parameters and returns a tuple containing the result of the roll and a boolean indicating whether the check was successful.

### Die(class)

The Die class is used to create a single die. The Die class has the following attributes:

* value
* last_roll

The Die class has the following methods:

* roll
* rolls
* flip(coin only)

#### Usage(Die)

```python
from dicepy import Die

d6 = Die(6)
d6.roll()
```

### d20(class)

The d20 class is a subclass of Die and is used to create a d20. The d20 class implements a special roll method called check, which accepts a modifier(mod) and difficulty class(dc) as parameters and returns a tuple containing the result of the roll and a boolean indicating whether the check was successful.

#### Usage(d20)

```python
from dicepy.Die import d20

d20 = d20()
d20.check(5, 15)
```

## Roll(submodule)

The Roll submodule contains the following functions for rolling dice:

* roll(die)
* rolls(die, num)
* roll_sequence(dice)
* flip(coin)
* check(d20, mod, dc)
* ability_roll
* ability_rolls
