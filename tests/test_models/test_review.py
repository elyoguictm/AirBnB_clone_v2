#!/usr/bin/python3
""" testing class """
import unittest
from models.base_model import BaseModel
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class TestReviewDocs(unittest.TestCase):
    """ testing class"""

    def test_pep8_conformance_review(self):
        """ testing pep8"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_review(self):
        """ testing pep8"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

        def test_review_module_docstring(self):
            """ testing pep8"""
            self.assertIsNot(review.__doc__, None,
                             "review.py needs a docstring")
            self.assertTrue(len(review.__doc__) >= 1,
                            "review.py needs a docstring")

        def test_review_class_docstring(self):
            """ testing pep8"""
            self.assertIsNot(Review.__doc__, None,
                             "Review class needs a docstring")
            self.assertTrue(len(Review.__doc__) >= 1,
                            "Review class needs a docstring")


class test_review(unittest.TestCase):
    """ testing class """
    @classmethod
    def setUpClass(cls):
        """testing class"""
        cls.rev = Review()
        cls.rev.place_id = "4321-dcba"
        cls.rev.user_id = "123-bca"
        cls.rev.text = "Holbert0n"

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', 'file')
    def test_save_Review(self):
        """ testing class """
        self.rev.save()
        self.assertNotEqual(self.rev.created_at, self.rev.updated_at)

    def teardown(cls):
        """ testing class """
        del cls.rev

    def test_str(self):
        """ testing class """
        review = Review()
        string = "[Review] ({}) {}".format(review.id, review.__dict__)
        self.assertEqual(string, str(review))
