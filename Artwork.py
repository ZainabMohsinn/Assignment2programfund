class Artwork:
    def __init__(self, title, artist, date, exhibitionLocation): #Here it shows the Artwork is sharing an object from the ExhibitioLocation
        self.title = title
        self.artist = artist
        self.date = date
        self.exhibitionLocation = exhibitionLocation

    def setTitle(self, title):
        self.title = title

    def getTitle(self):
        return self.title

    def setArtist(self, artist):
        self.artist = artist

    def getArtist(self):
        return self.artist

    def setDate(self, date):
        self.date = date

    def getDate(self):
        return self.date

    def setExhibitionLocation(self, exhibitionLocation):
        self.exhibitionLocation = exhibitionLocation

    def getExhibitionLocation(self):
        return self.exhibitionLocation


