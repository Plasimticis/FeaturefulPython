import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))) # lets us import ffpy from this directory, if you know a better way please let me know.
from ff import *
def greet(name: str) -> str:
    print(f"Hello {name}!")

eventManager = EventManager() # create eventmanager
eventManager.createEvent("GreetEvent") # create event
eventManager.bindEvent("GreetEvent", greet) # bind event to a function
# fire/call the binded event.
eventManager.fireEvent("GreetEvent", argument="mark") # output : 'Hello mark!'
# unbind it
eventManager.unbindEvent("GreetEvent")
# wont work.
eventManager.fireEvent("GreetEvent", argument="mark") # output : 'Event is not binded.'

eventManager.bindEvent("GreetEvent", greet) # rebind event to a function
# will work.
eventManager.fireEvent("GreetEvent", argument="mark") # output : 'Event is not binded.'
