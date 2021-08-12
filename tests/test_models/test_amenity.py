#!/usr/bin/python3
""" Unittest for Amenity """
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
import pep8


class pep8_test(unittest.TestCase):
    """ Test for the Amenity """
    def test_pep8_conformance_amenity(self):
        """Test that Amenity conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_tamenity(self):
        """Test that tAmenity conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_Amenity_module_docstring(self):
        """Test for the Amenity module docstring"""
        self.assertIsNot(__import__("Amenity").__doc__, None,
                         "amenity.py needs a docstring")
        self.assertTrue(len(__import__("Amenity").__doc__) >= 1,
                        "amenity.py needs a docstring")

    def test_Amenity_class_docstring(self):
        """Test for the Amenity class docstring"""
        self.assertIsNot(Amenity.__doc__, None,
                         "Amenity class needs a docstring")
        self.assertTrue(len(Amenity.__doc__) >= 1,
                        "Amenity class needs a docstring")
    
        def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)
