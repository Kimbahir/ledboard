class Ledboard():
    def __init__(self, x, y):
        """Initializes the board with X times Y
        Only allows single dot update to simulate a dumb led board

        Args:
            x (int): width of board
            y (int): height of board
        """
        self.x = x
        self.y = y
        self.board = [[False for i in range(self.x)] for l in range(self.y)]

    def on(self, x, y):
        """Sets a dot to True
        Note: it is to purposefully that I have reversed the X and Y to make it easier
        for me to read the output

        Args:
            x (int): x coordinate
            y (int): y coordinate
        """
        self.board[y][x] = True

    def off(self, x, y):
        """Sets a dot to True
        Note: it is to purposefully that I have reversed the X and Y to make it easier
        for me to read the output

        Args:
            x (int): x coordinate
            y (int): y coordinate
        """
        self.board[y][x] = False

    def toggle(self,x,y):
        """Flips the content of the dot at the given coordinate

        Args:
            x (int): x coordinate
            y (int): y coordinate
        """
        self.board[y][x] = not self.board[x][y]

    def print(self):
        """Returns a string that contains the content as dots
        """

        result = ""
        for x in self.board:
            for y in x:
                if y:
                    result += "*"
                else:
                    result += " "
            result += "\n"
        return result