class EventManager:
    def __init__(self) -> None:
        self.events = []
        self.bindedEvents = {}
        self.currentEvent = ""

    def createEvent(self, event: str) -> None:
        if self.currentEvent == event or event in self.events:
            print("Existing event.\n")
            return
        
        self.events.append(event)

    def bindEvent(self, event: str, func: callable) -> None:
        if event not in self.events:
            print("Event does not exist.\n")
            return
        
        self.bindedEvents[event] = func

    def fireEvent(self, event: str, argument=None) -> None:
        if event not in self.bindedEvents:
            print("Event is not binded.\n")
            return
        
        self.currentEvent = event
        try:
            if argument is not None:
                self.bindedEvents[event](argument)
            else:
                self.bindedEvents[event]()
        except Exception as e:
            print(f"Error executing event '{event}': {e}\n")

    def unbindEvent(self, event: str) -> None:
        if event in self.bindedEvents:
            del self.bindedEvents[event]
        else:
            print("Event is not binded.\n")
