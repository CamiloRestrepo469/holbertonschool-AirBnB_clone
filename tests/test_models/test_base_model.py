#!/usr/bin/python3
"""Test basemodel"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import models
import time
from unittest import mock
import json
import os
from models.engine.file_storage import FileStorage
import uuid


class TestBaseModel(unittest.TestCase):
    """test BaseModel class documentation and style"""

    def setUpClass(self):
        """Method set up instances"""
        pass

    def test_to_dict(self):
        """test the public instance method to_dict()"""
        m = BaseModel()
        m.name = "Holberton"
        m.number = 89
        b = m.to_dict()
        test_dict = ["id",
                     "created_at",
                     "updated_at",
                     "name",
                     "number",
                     "__class__"]
        self.assertCountEqual(b.keys(), test_dict)
        self.assertEqual(b['__class__'], 'BaseModel')
        self.asserEqual(b['name'], "Holberton")
        self.assertEqual(b['number'], 89)

    def test_time(self):
        """test  if times are of datetime instance"""
        self.assertIs(self.t1.updated_at.__class__, datetime)
        self.assertIs(self.t2.created_at.__class__, datetime)

    def test_str(self):
        """test correct output of str method"""
        ins = BaseModel()
        string = "[BaseModel] ({}) {}".format(ins.id, ins.__dict__)
        self.assertEqual(string, str(ins))

    def test_save(self):
        """test the save method"""
        first_update = self.obj.to_dict()
        self.obj.save()
        second_update = self.obj.to_dict()
        self.assertIs(self.obj.update_at.__class__, datetime)
        self.assertNotEqual(second_update["updated_at"],
                            first_update["updated_at"])

    def test_id(self):
        """test id of BaseModel instance"""
        obj = BaseModel()
        self.assertNotEqual(self.m.id, obj.id)
        print("{}".format(self.m.id))

    def test_kwargs(self):
        """test kwargs in BaseModel"""
        m_dict = self.dict.to_dict()
        obj = BaseModel(**m_dict)
        self.assertEqual(obj.to_dict(), self.dict.to_dict())

    def test_to_dict_values(self):
        """test the correct values"""
        dt_format = "%Y-%m-%dT%H:%M:%S.%f"
        m = BaseModel()
        new_dict = m.to_dict()
        self.assertEqual(new_dict["__class__"], "BaseModel")
        self.assertEqual(type(new_dict["crated_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(new_dict["crated_at"],
                         m.created_at.strftime(format))
        self.assertEqual(new_dict["updated_at"],
                         m.created_at.strftime(format))

    def test_uiid(self):
        """test that id is a valid uuid"""
        inst1 = BaseModel()
        inst2 = BaseModel()
        self.assertNotEqual(inst1.id, inst2.id)
        uuid = inst1.id
        with self.subTest(uuid=uuid):
            self.assertIs(type(uuid), str)

    @mock.patch('models.storage')
    def test_save(self, mock_storage):
        """test save and update at storage call"""
        inst = BaseModel()
        old_crated_at = inst.created_at
        old_updated_at = inst.updated_at
        inst.save()
        new_created_at = inst.created_at
        new_update_at = inst.updated_at
        self.assertNotEqual(old_updated_at, new_update_at)
        self.assertEqual(old_crated_at, new_created_at)
        self.assertEqual(mock_storage.save.called)


if __name__ == '__main__':
    unittest.main()
