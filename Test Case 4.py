from Ticket import Ticket
from ExhibitionLocation import ExhibitionLocation
from Visitor import Visitor

if __name__ == "__main__":
    location1 = ExhibitionLocation("Permanent galleries")
    location2 = ExhibitionLocation("Exhibition halls")
    location3 = ExhibitionLocation("Outdoor spaces")

    # Test case 4: Visitor with Ticket as Unidirectional Relationship
    def testVisitorWithTicket():
        try:
            visitorName = input("Enter visitor name: ")
            visitorAge = int(input("Enter visitor age: "))
            visitor = Visitor(visitorName, visitorAge)

            # Creating a ticket for an exhibition for the visitor to see
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

            # Creating the ticket with the specified details
            ticket = Ticket(visitor, exhibitionName, ticketPrice, location)

            # Displaying visitor and ticket details
            print("Visitor Details:")
            print("Name:", visitor.getName())
            print("Age:", visitor.getAge())
            print("Location:", location.getName())
            print("Ticket Details:")
            ticket.displayDetails()
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    testVisitorWithTicket()