class TicketingSystem:
    def __init__(self):
        self.tickets = []

class Ticket(TicketingSystem):
    def __init__(self, visitor, event, price, exhibitionLocation): #Here the ticket is sharing the object exhibitionLocation from the ExhibitionLocation
        super().__init__()
        self.visitor = visitor
        self.event = event
        self.price = price
        self.exhibitionLocation = exhibitionLocation

    def displayDetails(self):
        print(f"Visitor: {self.visitor.__str__()}, Event: {self.event}, Price: {self.price}, Location: {self.exhibitionLocation.getName()}")



