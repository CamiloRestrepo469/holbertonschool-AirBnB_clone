#!/usr/bin/python3
import unittest
from unittest.mock import mock_open, patch
import json
from datetime import datetime
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User
from models.state import State
from models.engine.file_storage import FileStorage
from os import path
import os


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_storage = FileStorage()

    def tearDown(self):
        # Elimina el archivo JSON creado durante las pruebas
        if path.exists(self.file_storage._FileStorage__file_path):
            os.remove(self.file_storage._FileStorage__file_path)

    def test_all(self):
        # Agrega algunos objetos a la instancia de FileStorage
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.file_storage.new(obj1)
        self.file_storage.new(obj2)

        # Comprueba que el método all() devuelve todos los objetos
        objects = self.file_storage.all()
        self.assertEqual(len(objects), 2)
        self.assertIn(f'{obj1.__class__.__name__}.{obj1.id}', objects)
        self.assertIn(f'{obj2.__class__.__name__}.{obj2.id}', objects)

    def test_new(self):
        # Agrega un objeto a la instancia de FileStorage
        obj = BaseModel()
        self.file_storage.new(obj)
        # Comprueba que el objeto se agregó correctamente
        objects = self.file_storage.all()
        self.assertIn(f'{obj.__class__.__name__}.{obj.id}', objects)
        self.assertEqual(objects[f'{obj.__class__.__name__}.{obj.id}'], obj)

    def test_save(self):
        # Agrega un objeto a la instancia de FileStorage
        obj = BaseModel()
        self.file_storage.new(obj)

        # Mockeo de la función open para capturar el contenido del archivo JSON
        with patch('builtins.open', mock_open()) as mock_file:
            self.file_storage.save()

            # Comprueba que la función open fue llamada con el archivo correcto
            mock_file.assert_called_once_with(
                self.file_storage._FileStorage__file_path, 'w')

            # Comprueba que se llamó a json.dump con los datos correctos
            mock_file().write(json.dumps(
                {f'{obj.__class__.__name__}.{obj.id}': obj.to_dict()}))

    def test_reload(self):
        self.assertEqual(self.storage.reload(), None)
        os.remove('file.json')


if __name__ == '__main__':
    unittest.main()
