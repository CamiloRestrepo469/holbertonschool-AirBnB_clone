#!/usr/bin/python3
import unittest
from models.city import City
from datetime import datetime
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    def test_inheritance(self):
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_attributes(self):
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_init_with_arguments(self):
        city = City(state_id="123", name="Test City")

        self.assertEqual(city.state_id, "123")
        self.assertEqual(city.name, "Test City")

    def test_init_with_kwargs(self):
        data = {
            'id': '123',
            'created_at': '2022-01-01T12:00:00.000000',
            'updated_at': '2022-01-02T12:00:00.000000',
            'state_id': '456',
            'name': 'Test City'
        }
        city = City(**data)

        self.assertEqual(city.id, '123')
        self.assertEqual(city.created_at, datetime.fromisoformat(
            '2022-01-01T12:00:00.000000'))
        self.assertEqual(city.updated_at, datetime.fromisoformat(
            '2022-01-02T12:00:00.000000'))
        self.assertEqual(city.state_id, '456')
        self.assertEqual(city.name, 'Test City')


if __name__ == '__main__':
    unittest.main()
