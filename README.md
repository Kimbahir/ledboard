# ledboard

Experiment with a virtual LED board for updating text string and optimizations

## Classes

ledboard

- Initializes with an X*Y size of dots
- Maintains the state of all dots
- To play with functionality, limited to only being able to set a dot to either ON, OFF or toggle between state

timetable

- Contains a set of lines, which contains the content that must be printed
- Contains a print function, that handles the calls to the ledboard

alphabet

- contains every letter in the alphabet, to a callable function

manager

- contains the different classes and ensures an abstraction layer for all the logic, so it can be simply updated