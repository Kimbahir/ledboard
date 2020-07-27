from app.ledboard import Ledboard
from app.timetable import Timetable
# l = Ledboard(5,4)
# l.on(0,0)
# l.on(0,3)
# l.on(2,0)
# print(l.print())

t = Timetable(3,5)
t.setTimeEntry(0,"ABC  ")
t.setTimeEntry(1,"  BBB")