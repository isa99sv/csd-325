# Colton Stone, December 20, 2025, Module 12.2 Assignment

import unittest
from city_functions import get_location

class LocationTest(unittest.TestCase):

    def test_city_country(self):
        location = get_location('Paris', 'France')
        self.assertEqual(location, 'Paris France')

unittest.main()