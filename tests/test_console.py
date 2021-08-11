#!/usr/bin/python3
""" Tests """
import pep8
import unittest
import cmd
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
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):
        """this will test the console"""

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style Werrors (and warnings).")

if __name__ == "__main__":
        unittest.main()
