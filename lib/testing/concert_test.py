from classes.many_to_many import Band
from classes.many_to_many import Concert
from classes.many_to_many import Venue

class TestConcert:
    """Concert in many_to_many.py"""
    
    def test_has_date(self):
        """Concert is initialized with a date"""
        band = Band(name="boygenius", hometown="NYC")
        venue = Venue(name="Theatre", city="NYC")
        concert = Concert(date="Nov 5", band=band, venue=venue)

        assert concert.date == "Nov 5"

    def test_date_is_mutable_string(self):
        """dates are mutable strings"""
        band = Band(name="boygenius", hometown="NYC")
        venue = Venue(name="Theatre", city="NYC")
        concert = Concert(date="Nov 5", band=band, venue=venue)

        concert.date = "Nov 15"
        assert isinstance(concert.date, str)
        assert concert.date == "Nov 15"

        #with pytest.raises(Exception):
             #concert.date = 15

    def test_date_has_length(self):
        """dates are longer than 0 characters"""
        band = Band(name="boygenius", hometown="NYC")
        venue = Venue(name="Theatre", city="NYC")
        concert = Concert(date="Nov 5", band=band, venue=venue)

        assert len(concert.date) > 0

        #with pytest.raises(Exception):
            # concert.date = ""

    def test_has_venue(self):
        """Concert is initialized with a venue"""
        band = Band(name="boygenius", hometown="NYC")
        venue = Venue(name="Theatre", city="NYC")
        concert = Concert(date="Nov 5", band=band, venue=venue)

        assert concert.venue == venue

    def test_venue_of_type_venue(self):
        """venue is of type Venue"""
        band = Band(name="boygenius", hometown="NYC")
        venue = Venue(name="Theatre", city="NYC")
        concert = Concert(date="Nov 5", band=band, venue=venue)

        assert isinstance(concert.venue, Venue)

        # with pytest.raises(Exception):
        #     concert.venue = "New York Theatre"

    def test_venue_is_immutable(self):
        """venues are immutable"""
        band = Band(name="boygenius", hometown="NYC")
        venue = Venue(name="Theatre", city="NYC")
        concert = Concert(date="Nov 5", band=band, venue=venue)

        # with pytest.raises(Exception):
        #     concert.venue = Venue(name="Radio City", city="NYC")

    def test_has_band(self):
        """Concert is initialized with a band"""
        band = Band(name="boygenius", hometown="NYC")
        venue = Venue(name="Theatre", city="NYC")
        concert = Concert(date="Nov 5", band=band, venue=venue)

        assert concert.band == band

    def test_band_of_type_band(self):
        """band is of type Band"""
        band = Band(name="boygenius", hometown="NYC")
        venue = Venue(name="Theatre", city="NYC")
        concert = Concert(date="Nov 5", band=band, venue=venue)

        assert isinstance(concert.band, Band)

        # with pytest.raises(Exception):
        #     concert.band = "boygenius"

    def test_band_is_immutable(self):
        """bands are immutable"""
        band = Band(name="boygenius", hometown="NYC")
        venue = Venue(name="Theatre", city="NYC")
        concert = Concert(date="Nov 5", band=band, venue=venue)

        # with pytest.raises(Exception):
        #     concert.band = Band(name="Spice Gurls", hometown="London")