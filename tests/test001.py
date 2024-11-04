import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))) # lets us import ffpy from this directory, if you know a better way please let me know.
from ff import *
eventManager = EventManager()
eventManager.createEvent("event")
def helloWorld(who: str) -> None:
    print(f"{who.capitalize()} Says: Hello world!")
def move() -> None:
    print("\n->no<-\n")
while True:
    i = int(input("What to do (1 = move 2 = print hello world 3 = exit): "))
    if i == 1:
        eventManager.bindEvent("event",move)
        eventManager.fireEvent("event")
        eventManager.unbindEvent("event")
    elif i == 2:
        eventManager.bindEvent("event",helloWorld)
        eventManager.fireEvent("event",argument="FeaturefulPython")
        eventManager.unbindEvent("event")
    elif i == 3:
        exit()