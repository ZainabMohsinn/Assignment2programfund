from ExhibitionLocation import ExhibitionLocation
class Exhibition:
    def __init__(self, title, duration, locationName):
        self.title = title
        self.duration = duration
        self.location = ExhibitionLocation(locationName)  # Composition: Exhibition contains an ExhibitionLocation

    def setTitle(self, title):
        self.title = title
    def getTitle(self):
        return self.title

    def setDuration(self, duration):
        self.duration = duration
    def getDuration(self):
        return self.duration

    def setLocation(self, location_name):
        self.location = ExhibitionLocation(location_name)
    def getLocation(self):
        return self.location.getName()

