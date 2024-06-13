from classes.many_to_many import Band
from classes.many_to_many import Concert
from classes.many_to_many import Venue

class TestVenue:
    """Venue in many_to_many.py"""
    
    def test_has_name(self):
        """Venue is instantiated with a name"""
        venue_1 = Venue(name="Webster Hall", city="NYC")
        venue_2 = Venue(name="Madison Square Garden", city="NYC")

        assert venue_1.name == "Webster Hall"
        assert venue_2.name == "Madison Square Garden"

    def test_name_is_mutable_string(self):
        """names are mutable strings"""
        venue_1 = Venue(name="Webster Hall", city="NYC")
        assert isinstance(venue_1.name, str)

        venue_1.name = "Madison Square Garden"
        assert isinstance(venue_1.name, str)
        assert venue_1.name == "Madison Square Garden"

        # with pytest.raises(Exception):
        #     venue_1.name = 7

    def test_name_has_length(self):
        """names are longer than 0 characters"""
        venue_1 = Venue(name="Webster Hall", city="NYC")
        assert len(venue_1.name) > 0

        # with pytest.raises(Exception):
        #     venue_1.name = ""

    def test_has_city(self):
        """Venue is instantiated with a city"""
        venue_1 = Venue(name="Webster Hall", city="NYC")
        venue_2 = Venue(name="Madison Square Garden", city="NYC")

        assert venue_1.city == "NYC"
        assert venue_2.city == "NYC"

    def test_city_is_immutable_string(self):
        """cities are immutable strings"""
        venue_1 = Venue(name="Webster Hall", city="NYC")
        assert isinstance(venue_1.city, str)

        # with pytest.raises(Exception):
        #     venue_1.city = "Boston"

        # with pytest.raises(Exception):
        #     venue_1.city = 7

        # with pytest.raises(Exception):
        #     Venue(name="Webster Hall", city=7)

    def test_city_has_length(self):
        """cities are longer than 0 characters"""
        venue_1 = Venue(name="Webster Hall", city="NYC")
        assert len(venue_1.city) > 0

        # with pytest.raises(Exception):
        #     venue_1.city = ""

    def test_concerts(self):
        """venue has many concerts"""
        venue = Venue(name="Webster Hall", city="NYC")
        band = Band(name="boygenius", hometown="NYC")
        concert_1 = Concert(date="Nov 22", band=band, venue=venue)
        concert_2 = Concert(date="Nov 27", band=band, venue=venue)

        assert len(venue.concerts()) == 2
        assert concert_1 in venue.concerts()
        assert concert_2 in venue.concerts()

    def test_concerts_of_type_concert(self):
        """concerts must be of type Concert"""
        venue = Venue(name="Webster Hall", city="NYC")
        band = Band(name="boygenius", hometown="NYC")
        Concert(date="Nov 22", band=band, venue=venue)
        Concert(date="Nov 27", band=band, venue=venue)

        assert all(isinstance(concert, Concert) for concert in venue.concerts())

    def test_bands(self):
        """venue has many bands"""
        venue = Venue(name="Webster Hall", city="NYC")
        band_1 = Band(name="boygenius", hometown="NYC")
        band_2 = Band(name="Spice Girls", hometown="London")
        Concert(date="Nov 22", band=band_1, venue=venue)
        Concert(date="Nov 27", band=band_2, venue=venue)

        assert len(venue.bands()) == 2
        assert band_1 in venue.bands()
        assert band_2 in venue.bands()

    def test_bands_of_type_band(self):
        """bands must be of type Band"""
        venue = Venue(name="Webster Hall", city="NYC")
        band_1 = Band(name="boygenius", hometown="NYC")
        band_2 = Band(name="Spice Girls", hometown="London")
        Concert(date="Nov 22", band=band_1, venue=venue)
        Concert(date="Nov 27", band=band_2, venue=venue)

        assert all(isinstance(band, Band) for band in venue.bands())

    def test_bands_are_unique(self):
        """bands are unique"""
        venue = Venue(name="Webster Hall", city="NYC")
        band_1 = Band(name="boygenius", hometown="NYC")
        band_2 = Band(name="Spice Girls", hometown="London")
        Concert(date="Nov 22", band=band_1, venue=venue)
        Concert(date="Nov 27", band=band_2, venue=venue)
        Concert(date="Nov 29", band=band_2, venue=venue)

        assert len(set(venue.bands())) == len(venue.bands())
        assert len(venue.bands()) == 2
        assert band_1 in venue.bands()
        assert band_2 in venue.bands()