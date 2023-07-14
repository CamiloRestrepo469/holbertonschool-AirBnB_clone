#!/usr/bin/python3
"""unittest for amenity"""
import unittest
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FilesStorage
import os


class TestCity(unittest.TestCase):
    """Test TestCyty class"""

    def setUp(self):
        """Test setUp method"""
        pass

    def test_attr(self):
        """test attributes correct types"""
        self.assertIs(self.city.state_id, str())
        self.assertIs(self.city.name, str())

    def test_str(self):
        """test str method"""
        amenity = City()
        string = "[City]({}){}".format(city.id, city.__dict__)
        self.assertEqual(string, str(city))


if __name__ == "__main__":
    unittest.main()
