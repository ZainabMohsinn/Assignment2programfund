from ExhibitionLocation import ExhibitionLocation
from TicketingSystem import TicketingSystem
from Visitor import Visitor

if __name__ == "__main__":
    location1 = ExhibitionLocation("Permanent galleries")
    location2 = ExhibitionLocation("Exhibition halls")
    location3 = ExhibitionLocation("Outdoor spaces")

# Test case 3: Ticket with TicketingSystem as Inheritance
def testTicketWithTicketingSystem():
    try:
        ticketingSystem = TicketingSystem()


        visitorName = input("Enter visitor name: ")
        visitorAge = int(input("Enter visitor age: "))
        visitor = Visitor(visitorName, visitorAge)
        exhibitionName = input("Enter exhibition name: ")
        ticketPrice = float(input("Enter ticket price: "))

        print("Choose location:")
        print("1. Permanent galleries")
        print("2. Exhibition halls")
        print("3. Outdoor spaces")
        choice = int(input("Enter your choice of the Exhibition Location (As a number): "))
        if choice == 1:
            location = location1
        elif choice == 2:
            location = location2
        elif choice == 3:
            location = location3
        else:
            raise ValueError("Invalid choice")

        ticket = ticketingSystem.generateTicket(visitor, exhibitionName, ticketPrice, location)
        print("Ticket Details:")
        print("Visitor:", ticket.visitor.getName())
        print("Exhibition:", ticket.event)
        print("Price:", ticket.price)
        print("Location:", ticket.exhibitionLocation.getName())
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    ticketingSystem = TicketingSystem()
    testTicketWithTicketingSystem()
