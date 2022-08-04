#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel
from uuid import uuid4
import time


class MyTestCase(unittest.TestCase):
    """Test class for models.base_model.BaseModel"""

    def test_if_BaseModel_instance_has_id(self):
        """Checks if the instance has an id attribute"""
        b = BaseModel()
        self.assertTrue(hasattr(b, 'id'))

    def test_str_represenation(self):
        """Checks if the string representation is appropriate"""
        b = BaseModel()
        self.assertEqual(str(b), "[BaseModel] ({}) {}".format(b.id, b.__dict__))

    def test_ids_unique(self):
        """checks if the generated ids are unique"""
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_type_of_id(self):
        """check if the type of the generated id is str"""
        b1 = BaseModel()
        self.assertTrue(type(b1.id) is str)

    def test_created_at_is_datetime_object(self):
        """checks if the created_at attribute is a datetime object"""
        b = BaseModel()
        self.assertTrue(type(b.created_at) is datetime)

    def test_update_at_is_datetime_object(self):
        """checks if the updated at attribute is datetime object"""
        b = BaseModel()
        self.assertTrue(type(b.updated_at) is datetime)

    def test_if_twoModels_have_different_created_at(self):
        """checks if two models have different created_at"""
        b = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b.created_at, b2.created_at)

    def test_created_at_isEqual_with_updated_at(self):
        """checks if created_at is equal to updated at initially"""
        b = BaseModel()
        self.assertEqual(b.created_at, b.updated_at)

    def test_args_unused(self):
        """checks if args are unused"""
        b1 = BaseModel(None)
        self.assertNotIn(None, b1.__dict__.values())

    def test_if_two_models_have_different_created_at(self):
        """checks that two models have different id"""
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.created_at, b2.created_at)

    def test_that_save_func_update_update_at_attr(self):
        """checks that the save function updates the updated_at attribute"""
        b1 = BaseModel()
        b1.save()
        self.assertNotEqual(b1.created_at, b1.updated_at)

    def test_to_dict_returns_a_dict(self):
        """checks if the to_dict methods returns a dict"""
        b1 = BaseModel()
        self.assertTrue(type(b1.to_dict() is dict))

    def test_if_to_dict_adds_dunder_to_dict(self):
        """checks if to_dict adds __class__ is added to dict"""
        b1 = BaseModel()
        self.assertTrue('__class__' in b1.to_dict())

    def test_that_created_at_returned_by_to_dict_is_iso_string(self):
        """checks that created_at is stored as a str obj in ISO format"""
        b1 = BaseModel()
        b1.to_dict()
        self.assertNotEqual(type(b1.created_at), type(b1.created_at.isoformat()))

    def test_when_kwargs_passed_empty(self):
        """checks that id, created_At, updated are automatically generated
        if they aren't strings
        """
        my_dict = {}
        b = BaseModel()
        self.assertTrue(type(b.id) is str)
        self.assertTrue(type(b.created_at) is datetime)
        self.assertTrue(type(b.updated_at) is datetime)

    def test_when_kwargs_is_not_empty(self):
        """checks id, created_at, updated, are created from kwargs"""
        my_dict = {"id": uuid4(), "created_at": datetime.utcnow().isoformat(),
                   "updated_at": datetime.utcnow().isoformat()}
        b = BaseModel(**my_dict)
        self.assertEqual(b.id, my_dict['id'])


if __name__ == '__main__':
    unittest.main()
