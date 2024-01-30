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
