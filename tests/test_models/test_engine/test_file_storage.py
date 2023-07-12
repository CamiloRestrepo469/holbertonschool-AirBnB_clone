#!/usr/bin/python3
""" Tets from file storage
"""


import unittest
from unittest.mock import mock_open, patch
import json
import os
from models.base_model import BaseModel
import models
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_storage = FileStorage()

    def tearDown(self):
        # Elimina el archivo JSON creado durante las pruebas
        if os.path.exists(self.file_storage._FileStorage__file_path):
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
    
    def test_save(self):
        # Agrega un objeto a la instancia de FileStorage
        obj = BaseModel()
        self.file_storage.new(obj)

        # Mockeo de la función open para capturar el contenido del archivo JSON
        with patch('builtins.open', mock_open()) as mock_file:
            self.file_storage.save()

            # Comprueba que la función open fue llamada con el archivo correcto
            mock_file.assert_called_once_with(self.file_storage._FileStorage__file_path, 'w')

            # Comprueba que se llamó a json.dump con los datos correctos
            mock_file().write.assert_called_once_with(json.dumps({f'{obj.__class__.__name__}.{obj.id}': obj.to_dict()}))

    def test_reload(self):
        # Crea un archivo JSON con un objeto guardado
        data = {
            'BaseModel.123456': {
                'id': '123456',
                'name': 'objeto1',
                # ...otros atributos...
            }
        }
        with open(self.file_storage._FileStorage__file_path, 'w') as file:
            json.dump(data, file)

        # Llama al método reload() para cargar los objetos en la instancia de FileStorage
        self.file_storage.reload()
        
        # Comprueba que el objeto se cargó correctamente
        objects = self.file_storage.all()
        self.assertEqual(len(objects), 1)
        self.assertIn('BaseModel.123456', objects)
        self.assertEqual(objects['BaseModel.123456'].name, 'objeto1')


if __name__ == '__main__':
    unittest.main()