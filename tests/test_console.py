#!/usr/bin/python3
""" Contains the class TestConsoleDocs """

import pep8
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage
from os import getenv
from console import HBNBCommand


class pep8_test(unittest.TestCase):
    """pep8 test cases class"""
    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style Werrors (and warnings).")


    def test_console_module_docstr(self):
        """Test for the console.py module docstring"""
        self.assertIsNot(__import__("console").__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(len(__import__("console").__doc__) >= 1,
                        "console.py needs a docstring")

    def test_HBNBCommand_class_docstr(self):
        """Test for the HBNBCommand class docstring"""
        self.assertIsNot(HBNBCommand.__doc__, None,
                         "HBNBCommand class needs a docstring")
        self.assertTrue(len(HBNBCommand.__doc__) >= 1,
                        "HBNBCommand class needs a docstring")
