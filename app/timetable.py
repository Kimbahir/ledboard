"""Maintaining overall state
"""
import sys
import pygame
from alphabet import Alphabet
from ledboard import Ledboard
#from pygame.locals import *


class Timetable():
    """Class to maintain the state of the timetable
    """

    def __init__(self, rows, columns):
        """Timetable contains representation of the strings that are shown and manages all updates

        Args:
            rows (int): number of lines (strings) perceived by user on the led board
            columns (int): number of chars per line
        """
        self.ledboard = Ledboard(columns*(5+1), rows*(7+1))
        self.rows = rows
        self.columns = columns
        self.times = [[" " for col in columns] for row in rows]
        self.dotsize = 6
        self.alphabet = Alphabet()

        pygame.init()
        while True:
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    def set_time_entry(self, position, entry):
        """Sets the time entry at a given position

        Args:
            position (int): 0 based entry position
            entry (str): string to be shown
        """
        self.times[position] = entry

    def update(self):
        """Updates the LED board
        """
        for r_idx, time in enumerate(self.times):
            print(f"{r_idx} {time}")

    def print(self):
        """Prints the current state to the console
        """
        print(self.alphabet.A)
