from alphabet import Alphabet
from ledboard import Ledboard 

class Timetable():
    def __init__(self, rows, columns):
        """Timetable contains representation of the strings that are shown and manages all updates

        Args:
            rows (int): number of lines (strings) perceived by user on the led board
            columns (int): number of chars per line
        """
        self.ledboard = Ledboard(columns*(5+1), rows*(7+1))
        self.times = [[" " for col in columns] for row in rows]

    def setTimeEntry(self, position, entry):
        self.times[position] = entry

    def update(self):
        for rIdx, time in enumerate(self.times):
            print(f"{rIdx} {time}")

    def print(self):
        pass