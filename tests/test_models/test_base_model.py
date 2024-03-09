#!/usr/bin/python3
import datetime
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """
    Test cases of the BaseModel.

    """
    def setUp(self):
        """
        innitilizes instance testing BaseModel.

        """
        self.base_model= BaseModel()

    def test_id_str(self):
        """
        confirming id is string

        """
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_datetime(self):
        """
        confirming if created time is datetime.

        """
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_datetime(self):
        """
        confirming if updated time is datetime.

        """
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_str(self):
        """
        confirming id __str__ method returns string.

        """
        str_rep = str(self.base_model)
        self.assertIsInstance(str_rep, str)

    def test_save(self):
        """
        confirming the save method work.

        """
        or_updated_at = self.base_model.updated_at
        self.base_model.save()
        nw_updated_at = self.base_model.updated_at
        self.assertNotEqual(or_updated_at, nw_updated_at)

    def test_to_dict(self):
        """
        testing the to_dict method.

        """
        dict_rp = self.base_model.to_dict()
        self.assertIsInstance(dict_rp, dict)

if __name__ == "__main__":
    unittest.main()
