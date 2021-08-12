#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State
import unittest
from models.user import User
import pep8

class test_state(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_pep8_console(self):
        '''test pep8 style'''
        s = pep8.StyleGuide(quiet=True)
        pep = s.check_files(['models/state.py'])
        self.assertEqual(pep.total_errors, 0, 'Found errors.')

    def test_user(self):
        '''Test for State'''
        s = State(name='Of Mind')
        self.assertEqual(str, type(s.name))


if __name__ == '__main__':
    unittest.main()
