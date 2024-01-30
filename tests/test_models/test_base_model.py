#!/usr/bin/python3

import unittest
import uuid
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):

    def test_attributes(self):
        obj = BaseModel()
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))

    def test_id_generate(self):
        obj = BaseModel()
        self.assertTrue(isinstance(obj.id, str))
        self.assertTrue(uuid.UUID(obj.id, version=4))

    def test_save_method(self):
        obj = BaseModel()
        currently_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(currently_updated_at, obj.updated_at)

    def test_dict(self):
        obj = BaseModel()
        obj_dict = obj.to_dict()

        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertEqual(obj_dict['__class__'], obj.__class__.__name__)
        self.assertIn('id', obj_dict)
        self.assertEqual(obj_dict['id'], obj.id)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)

        created_at_str = datetime.strptime(obj_dict['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
        updated_at_str = datetime.strptime(obj_dict['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")

        self.assertEqual(created_at_str, obj.created_at)
        self.assertEqual(updated_at_str, obj.updated_at)

    def test_str_method(self):
        obj = BaseModel()
        expected_str = f"[{obj.__class__.__name__}] ({obj.id}) {obj.__dict__}"
        self.assertEqual(str(obj), expected_str)


