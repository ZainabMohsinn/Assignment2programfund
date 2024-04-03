from Exhibition import Exhibition
from ExhibitionLocation import ExhibitionLocation

location1 = ExhibitionLocation("Permanent galleries")
location2 = ExhibitionLocation("Exhibition halls")
location3 = ExhibitionLocation("Outdoor spaces")


# Test case 2: Exhibition with ExhibitionLocation as Composition
def testExhibitionWithExhibitionLocation():
    try:
        title = input("Enter exhibition title: ")
        duration = input("Enter exhibition duration: ")

        # Choose from predefined locations
        print("Choose location:")
        print("1. Permanent galleries")
        print("2. Exhibition halls")
        print("3. Outdoor spaces")
        choice = input("Enter your choice of the Exhibition Location (As a number): ")

        if choice == '1':
            exhibition_location = location1
        elif choice == '2':
            exhibition_location = location2
        elif choice == '3':
            exhibition_location = location3
        else:
            raise ValueError("Exhibition cannot exist without an associated ExhibitionLocation.")


        exhibition = Exhibition(title, duration, exhibition_location)
        print("Exhibition Details:")
        print("Title:", exhibition.getTitle())
        print("Duration:", exhibition.getDuration())
        print("Location:", exhibition.getLocation().getName())
    except Exception as e:
        print("Exhibition cannot exist without an associated ExhibitionLocation.", e)


if __name__ == "__main__":
    testExhibitionWithExhibitionLocation()

#The exception code is used to handle cases where an Exhibition object is
# created without an ExhibitionLocation to show the relationship between Exhibition
# and ExhibitionLocation as composition where it shows that the Exhibition
# can't exist unless Exhibition Location is created, and since the code will show an error
# we used the Exception handling since we want to avoid program crashes.