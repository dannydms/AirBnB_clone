#!/usr/bin/python3
general classes tests
"""
Unittest for amenity.py
"""
import unittest
general classes tests
from models.amenity import Amenity
general classes tests
import datetime
general classes tests
general classes tests
class TestAmenity(unittest.TestCase):
    """Tests instances and methods from amenity class"""
general classes tests
general classes tests
    a = Amenity()
general classes tests
general classes tests
    def test_class_exists(self):
        """tests if class exists"""
        res = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(self.a)), res)
    def test_user_inheritance(self):
        """test if Amenity is a subclass of BaseModel"""
        self.assertIsInstance(self.a, Amenity)
    def testHasAttributes(self):
        """verify if attributes exist"""
        self.assertTrue(hasattr(self.a, 'name'))
        self.assertTrue(hasattr(self.a, 'id'))
        self.assertTrue(hasattr(self.a, 'created_at'))
        self.assertTrue(hasattr(self.a, 'updated_at'))
    def test_types(self):
        """tests if the type of the attribute is the correct one"""
        self.assertIsInstance(self.a.name, str)
        self.assertIsInstance(self.a.id, str)
        self.assertIsInstance(self.a.created_at, datetime.datetime)
        self.assertIsInstance(self.a.updated_at, datetime.datetime)
if __name__ == '__main__':
    unittest.main()
