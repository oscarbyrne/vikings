from events import EventController
from frames import TestFrame

gstate = object()
cont = EventController(gstate)


cont.execute_frame(TestFrame)
