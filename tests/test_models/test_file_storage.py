import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_path = "test_file.json"
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.file_path

    def tearDown(self):
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass

    def test_all(self):
        objects = self.storage.all()
        self.assertIsInstance(objects, dict)
        self.assertEqual(len(objects), 0)

    def test_new(self):
        obj = BaseModel()
        self.storage.new(obj)
        objects = self.storage.all()
        self.assertEqual(len(objects), 1)
        self.assertIn(f"BaseModel.{obj.id}", objects)

    def test_save_reload(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        new_storage = FileStorage()
        new_storage._FileStorage__file_path = self.file_path
        new_storage.reload()
        objects = new_storage.all()
        self.assertEqual(len(objects), 1)
        self.assertIn(f"BaseModel.{obj.id}", objects)

    def test_base_model_init(self):
        obj = BaseModel(name="Test", age=25)
        self.assertEqual(obj.name, "Test")
        self.assertEqual(obj.age, 25)

    def test_base_model_save(self):
        obj = BaseModel()
        self.assertIsNone(obj.updated_at)
        obj.save()
        self.assertIsNotNone(obj.updated_at)


if __name__ == "__main__":
    unittest.main()
