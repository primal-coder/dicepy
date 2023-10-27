# dicepy

A Python library for working with dice. This library is intended to be used for tabletop roleplaying games.
Dicepy is composed of three submodules: 'Dice', 'Die' and 'Roll'. 

## Installation

```bash
pip install dicepy
```

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

### roll(die)

The roll function is used to roll a single die. The roll function accepts a Die object as a parameter and returns the result of the roll.

#### Usage(roll)

```python
from dicepy.Roll import roll
from dicepy.Dice import DiceSet
dset = DiceSet()

roll(dset.d6)
# output: 4
roll(6)
# output: 4
roll('d6')
# output: 4
```

### rolls(die, num, dstr)

The rolls function is used to roll a single die multiple times. The rolls function accepts a Die object and an integer as parameters and returns the sum of the results of the rolls.

#### Usage(rolls)

```python
from dicepy.Roll import rolls
from dicepy.Dice import DiceSet
dset = DiceSet()

rolls(3, dset.d6)
# output: 12
rolls(3, 6)
# output: 12
rolls(3, 'd6')
# output: 12
```

### roll_sequence(dice)

The roll_sequence function is used to roll a sequence of dice. The roll_sequence function accepts the same parameters as the rolls function and returns a tuple containing the results of the rolls.

#### Usage(roll_sequence)

```python
from dicepy.Roll import roll_sequence
from dicepy.Dice import DiceSet
dset = DiceSet()

roll_sequence(3, dset.d6)
# output: (4, 2, 6)
roll_sequence(3, 6)
# output: (4, 2, 6)
roll_sequence(3, 'd6')
# output: (4, 2, 6)
```

### flip(coin)

The flip function is used to flip a coin. The flip function accepts no parameters and returns the result of the flip.

#### Usage(flip)

```python
from dicepy.Roll import flip
from dicepy.Dice import DiceSet
dset = DiceSet()

flip(dset.coin)
# output: heads
flip('coin')
# output: heads
```

### check(d20, mod, dc)

The check function is used to roll a d20 and compare the result to a difficulty class. The check function accepts a d20 object, an integer and an integer as parameters and returns a tuple containing the result of the roll and a boolean indicating whether the check was successful.

#### Usage(check)

```python
from dicepy.Roll import check
from dicepy.Dice import DiceSet
dset = DiceSet()

check(5, 15)
# output: (17, True)
```

### ability_roll

The ability_roll function is used to generate an ability score. The ability_roll function accepts no parameters and returns a tuple containing a list of the five d6 roll results and the sum of the three highest rolls.

#### Usage(ability_roll)

```python
from dicepy.Roll import ability_roll

ability_roll()
# output: ([4, 2, 6, 1, 3], 14)
```

### ability_rolls

The ability_rolls function is used to generate a set of ability scores. The ability_rolls function accepts no argument and returns a list of 6 integers, each representing the sum of the three highest rolls of a set of five d6 rolls. If the expunge argument is set to True and the list contains a score lower than 12 the list is discarded and a new list is generated.

#### Usage(ability_rolls)

```python
from dicepy.Roll import ability_rolls

ability_rolls(expunge=False)
# output: [14, 13, 12, 10, 9, 8]
ability_rolls(expunge=True)
# output: [16, 14, 13, 13, 12, 12]
```

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Contact

[Email](mailto:joesaysahoy@gmail.com)
[github](https://github.com/primal-coder)
[facebook](https://facebook.com/joesaysahoy)

### Support

[buymeacoffe](https://www.buymeacoffee.com/primalcoder)