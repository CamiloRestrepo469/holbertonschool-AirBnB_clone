import unittest
from models import Place


class PlaceTest(unittest.TestCase):

    def test_place_initialization(self):
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_place_attributes(self):
        place = Place()
        place.city_id = "12345"
        place.user_id = "67890"
        place.name = "Cozy Cottage"
        place.description = "A charming cottage in the countryside"
        place.number_rooms = 2
        place.number_bathrooms = 1
        place.max_guest = 4
        place.price_by_night = 100
        place.latitude = 42.1234
        place.longitude = -71.5678
        place.amenity_ids = [1, 2, 3]
        self.assertEqual(place.city_id, "12345")
        self.assertEqual(place.user_id, "67890")
        self.assertEqual(place.name, "Cozy Cottage")
        self.assertEqual(place.description,
                         "A charming cottage in the countryside")
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 42.1234)
        self.assertEqual(place.longitude, -71.5678)
        self.assertEqual(place.amenity_ids, [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
