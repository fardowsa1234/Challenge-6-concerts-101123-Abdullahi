class Band:
    def __init__(self, name, hometown):
        self.name = name
        self._hometown = hometown
        self._concerts = []

    @property
    def hometown(self):
        return self._hometown

    @hometown.setter
    def hometown(self, value):
        raise AttributeError("hometown is immutable")

    def concerts(self):
        return self._concerts

    def play_in_venue(self, venue, date):
        concert = Concert(date=date, band=self, venue=venue)
        print(f"Band.play_in_venue: Created concert on {date} at {venue.name} for {self.name}")
        return concert

    def venues(self):
        return list({concert.venue for concert in self._concerts})

    def all_introductions(self):
        introductions = [
            f"Hello {concert.venue.city}!!!!! We are {self.name} and we're from {self.hometown}"
            for concert in self._concerts
        ]
        print(f"Band.all_introductions: {introductions}")
        return introductions


class Concert:
    def __init__(self, date, band, venue):
        self.date = date
        self._band = band
        self._venue = venue
        if self not in band.concerts():
            band.concerts().append(self)
        if self not in venue.concerts():
            venue.concerts().append(self)
        print(f"Concert.__init__: Concert on {date} at {venue.name} for {band.name}")

    @property
    def band(self):
        return self._band

    @band.setter
    def band(self, value):
        raise AttributeError("band is immutable")

    @property
    def venue(self):
        return self._venue

    @venue.setter
    def venue(self, value):
        raise AttributeError("venue is immutable")


class Venue:
    def __init__(self, name, city):
        self.name = name
        self._city = city
        self._concerts = []

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        raise AttributeError("city is immutable")

    def concerts(self):
        return self._concerts

    def bands(self):
        return list({concert.band for concert in self._concerts})
