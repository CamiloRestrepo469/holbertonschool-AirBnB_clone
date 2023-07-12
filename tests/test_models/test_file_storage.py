import unittest
import json
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.file_path = "file.json"
        # Create an instance of the FileStorage class
        self.storage = FileStorage()

    def tearDown(self):
        # Remove the file created during testing
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_store_first_object(self):
        # Create a BaseModel instance
        obj = BaseModel()
        # Store the object using the FileStorage instance
        self.storage.new(obj)
        self.storage.save()

        # Load the stored data from the file
        with open(self.file_path, "r") as file:
            data = json.load(file)

        # Verify that the object was stored correctly
        self.assertIn(f"BaseModel.{obj.id}", data)

    def test_all_method(self):
        # Create a BaseModel instance
        obj = BaseModel()
        self.storage.new(obj)

        # Get all objects using the all() method
        all_objects = self.storage.all()

        # Verify that the object is in the returned dictionary
        self.assertIn(f"BaseModel.{obj.id}", all_objects)

    # Add more test cases for other methods...

if __name__ == '__main__':
    unittest.main()
