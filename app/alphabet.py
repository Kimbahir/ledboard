"""The alphabet class
"""


class Alphabet():
    """Holding the 5x7 alphabet for all chars
    """

    def __init__(self):
        """Initialized the alphabet, so it can be picked up and used for drawing
        """
        self.empty = [
            "     ",
            "     ",
            "     ",
            "     ",
            "     ",
            "     ",
            "     "
        ]
        self.a_char = [
            " *** ",
            "*   *",
            "*   *",
            "*   *",
            "*****",
            "*   *",
            "*   *"
        ]
        self.b_char = [
            "**** ",
            "*   *",
            "*   *",
            "**** ",
            "*   *",
            "*   *",
            "**** "
        ]
        self.c_char = [
            " *** ",
            "*   *",
            "*    ",
            "*    ",
            "*    ",
            "*   *",
            " *** "
        ]
