#!/usr/bin/python3
""" Unittest for BaseModel """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os
import pep8
import unittest
import os
from os import getenv
from models import storage
from models.state import State
import MySQLdb


class test_basemodel(unittest.TestCase):
    """ Test for BaseModel """

    def test_pep8_BaseModel(self):
        """Testing for pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_module_docstring(self):
        """Test for the existence of module docstring"""
        self.assertIsNot(module_doc, None,
                         "base_model.py needs a docstring")
        self.assertTrue(len(module_doc) > 1,
                        "base_model.py needs a docstring")

    def test_class_docstring(self):
        """Test for the BaseModel class docstring"""
        self.assertIsNot(BaseModel.__doc__, None,
                         "BaseModel class needs a docstring")
        self.assertTrue(len(BaseModel.__doc__) >= 1,
                        "BaseModel class needs a docstring")

    def __init__(self, *args, **kwargs):
        """ Test for BaseModel """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ Test for BaseModel """
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """ Test for BaseModel """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ Test for BaseModel """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ Test for BaseModel """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """ Test for BaseModel """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """ Test for BaseModel """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ Test for BaseModel """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_id(self):
        """ Test for BaseModel """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ Test for BaseModel """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ Test for BaseModel """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)
