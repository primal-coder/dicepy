from ._die import Die as _Die, d20 as _d20

_std_set = {
    'coin': 2,
    'd4': 4,
    'd6': 6,
    'd8': 8,
    'd10': 10,
    'd12': 12,
    'd20': 20
}

# Create all the die
class DiceSet:
    """
    DiceSet class representative of a set of dice. The class has attributes for each type of die. Creates a set of
    dice with the following attributes: coin, d4, d6, d8, d10, d12, d20. Each attribute is a Die object with the
    appropriate number of sides. The d20 attribute is a d20 object. This allows for the creation of independent sets
    of dice(i.e., dice_set_1 = DiceSet() and dice_set_2 = DiceSet())
    
    Attributes:
        coin (Die): A Die object with two sides, representing a coin.
        d4 (Die): A Die object with four sides.
        d6 (Die): A Die object with six sides.
        d8 (Die): A Die object with eight sides.
        d10 (Die): A Die object with ten sides.
        d12 (Die): A Die object with twelve sides.
        d20 (d20): A d20 object with twenty sides.
    """

    def __init__(self, dice: dict = _std_set):
        for die in dice:
            if not die.startswith('d') and die != 'coin' and die[0].isnumeric():
                for i in range(int(die[0])):
                    setattr(self, f'{die[1:]}_{"abcdef"[i]}', _Die(dice[die]))
            elif die != 'd20':
                setattr(self, die, _Die(dice[die]))
            else:
                setattr(self, die, _d20())
