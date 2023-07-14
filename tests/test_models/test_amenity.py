#!/usr/bin/python3
"""unittest for amenity"""
import unittest
from models.amenity import Amenity
from datetime import datetime
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    def test_inheritance(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)

    def test_attributes(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_init_with_arguments(self):
        amenity = Amenity(name="Test Amenity")
        self.assertEqual(amenity.name, "Test Amenity")

    def test_init_with_kwargs(self):
        data = {
            'id': '123',
            'created_at': '2022-01-01T12:00:00.000000',
            'updated_at': '2022-01-02T12:00:00.000000',
            'name': 'Test Amenity'
            }
        amenity = Amenity(**data)

        self.assertEqual(amenity.id, '123')
        self.assertEqual(amenity.created_at, datetime.fromisoformat('2022-01-01T12:00:00.000000'))
        self.assertEqual(amenity.updated_at, datetime.fromisoformat('2022-01-02T12:00:00.000000'))
        self.assertEqual(amenity.name, 'Test Amenity')


if __name__ == '__main__':
    unittest.main()
