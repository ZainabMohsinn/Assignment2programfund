from Artwork import Artwork
from ExhibitionLocation import ExhibitionLocation

if __name__ == "__main__":
    location1 = ExhibitionLocation("Permanent galleries")
    location2 = ExhibitionLocation("Exhibition halls")
    location3 = ExhibitionLocation("Outdoor spaces")


# Test case 1: Artwork with ExhibitionLocation as Aggregation
def testArtworkWithExhibitionLocation():
    try:
        title = input("Enter artwork title: ")
        artist = input("Enter artist name: ")
        date = input("Enter artwork date: ")
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
            raise ValueError("Invalid choice make sure you choose one of those 3 numbers and didn't write a string")

        artwork = Artwork(title, artist, date, location)
        print("Artwork Details:")
        print("Title:", artwork.getTitle())
        print("Artist:", artwork.getArtist())
        print("Date:", artwork.getDate())
        print("Location:", location.getName())
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    testArtworkWithExhibitionLocation()

#This code will handle any exceptions that might occur during the creation of
# the Artwork object without an associated ExhibitionLocation, which will allow the program to
# continue execution without crashing.