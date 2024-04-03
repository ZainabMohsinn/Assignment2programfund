from Ticket import *
class TicketingSystem:
    def __init__(self):
        self.tickets = []

    def generateTicket(self, visitor, event, price, exhibitionLocation):
        ticket = Ticket(visitor, event, price, exhibitionLocation)
        self.tickets.append(ticket)
        return ticket

