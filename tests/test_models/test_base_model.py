import unittest
from datetime import datetime
from unittest.mock import patch
import models
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def test_init_with_arguments(self):
        # Crea una instancia de BaseModel con argumentos
        data = {
            'id': '123456',
            'created_at': '2022-01-01T12:00:00.000000',
            'updated_at': '2022-01-02T12:00:00.000000',
            'name': 'objeto1',
            # ...otros atributos...
        }
        base_model = BaseModel(**data)

        # Comprueba que los atributos se hayan establecido correctamente
        self.assertEqual(base_model.id, '123456')
        self.assertEqual(base_model.created_at, datetime.fromisoformat(
            '2022-01-01T12:00:00.000000'))
        self.assertEqual(base_model.updated_at, datetime.fromisoformat(
            '2022-01-02T12:00:00.000000'))
        self.assertEqual(base_model.name, 'objeto1')

    def test_init_without_arguments(self):
        # Comprueba que se generen correctamente los atributos por defecto
        self.assertIsInstance(self.base_model.id, str)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_update(self):
        # Actualiza el modelo y comprueba que se actualice la fecha de actualización
        original_updated_at = self.base_model.updated_at
        self.base_model.update()
        self.assertNotEqual(original_updated_at, self.base_model.updated_at)

    def test_save(self):
        # Mockeo del método save de models.storage
        with patch.object(models.storage, 'save') as mock_save:
            self.base_model.save()
            # Comprueba que se llamó al método save de models.storage
            mock_save.assert_called_once()

    def test_to_dict(self):
        # Establece atributos en el modelo
        self.base_model.name = 'objeto1'
        self.base_model.value = 10

        # Genera el diccionario a partir del modelo
        model_dict = self.base_model.to_dict()
        # Comprueba que los atributos se hayan convertido correctamente en el diccionario
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], self.base_model.id)
        self.assertEqual(model_dict['created_at'],
                         self.base_model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'],
                         self.base_model.updated_at.isoformat())
        self.assertEqual(model_dict['name'], 'objeto1')
        self.assertEqual(model_dict['value'], 10)


if __name__ == '__main__':
    unittest.main()
