import random


def recursion_random_exclude(exclude, columns, amount):
    """A recursive Method to create an array of random tile positions/indices
    until no tile is created on any input indices (array of indices).

       :argument exclude: array of indices/positions to exclude.
       :argument columns: length of the array.
       :argument amount: how many tiles should be created in the roe.
       :return rng: the generated row.

       """

    rng = random.sample(range(columns), amount)
    is_excluded = True
    for i in rng:
        if i in exclude:
            is_excluded = False

    if not is_excluded:
        return recursion_random_exclude(exclude, columns, amount)
    else:
        return rng


class LevelGenerator:
    """A class to generate a level of tiles: an array of 1's -> tile and 0's -> no tile)
    Could be extended with a function to load handmade levels (arrays)

        Attributes:
            columns (int): Saves the length of the array
            length (int): Saves the number of arrays.
            content(list[list[int]]):
            max_tile_per_row (float):
    """
    def __init__(self, columns, length):
        """Holds parameters and attributes of the LevelGenerator class.

        :param columns: The length of the array.
        :param length: The number of arrays.

        """

        self.columns = columns
        self.length = length
        self.content = [[0 for x in range(self.columns)] for y in range(self.length)]
        self.max_tile_per_row = self.columns / 2

    @staticmethod
    def next_cycle(columns, max_amount, force_max, exclude):
        """Static method for infinite rows if no start or end is needed you can call this function
        to generate an array of 0,1. Because this method is static, the LevelGenerator class mustn't be
        initialized/constructed.

        :argument columns: array length.
        :argument max_amount: of tiles in a row.
        :argument force_max: if there should always be the max amount of tiles.
        :argument exclude: positions/indices where no tile should be created.
        :return row: generated row.

        """

        row = []
        if force_max:
            amount = max_amount
        else:
            amount = random.randint(1, max_amount)

        for i in range(columns):
            row.append(0)

        tile_indices = recursion_random_exclude(exclude, columns, amount)
        for i in tile_indices:
            row[i] = 1

        return row
