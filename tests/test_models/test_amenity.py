#!/usr/bin/python3
"""unittest for amenity"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
import os


class testAmenity(unittest.TestCase):
    """test Amenity class"""

    def setUp(self):
        """test Set method"""
        pass

    def test_attr(self):
        """test attributes correct types"""
        self.assertIs(self.amenity.name, st())

    def test_str(self):
        """test str method"""
        amenity = Amenity()
        string = "[Amenity]({}){}".format(amenity.id, amenity.__dict__)
        self.assertEqual(string, str(amenity))


if __name__ == "__main__":
    unittest.main()
