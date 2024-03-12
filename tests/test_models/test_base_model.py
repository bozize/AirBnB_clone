#!/usr/bin/python3
import os
import models
import unittest
from time import sleep
from models.base_model import BaseModel


class TestBaseModel(unittest.Test.Case):
    """the BaseModel testcase."""

    def setUp(self):
        """ setting up the test environment."""
        try:
            os.rename("fle.json", "tmp")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_base_model_inst(self):
        """BaseModel instantiation Testing."""
        ts1 = BaseModel()
        ts2 = BaseModel()
        self.assertNotEqual(ts1.id, ts2.id)
        self.assertLess(ts1.created_at, ts2.created_at)
        self.asserless(ts1.updated_at, ts2.updated_at)

    def test_save(self):
        """Save method Test."""
        ts = BaseModel()
        first_updated_at = ts.updated_at
        sleep(0.05)
        ts.save()
        self.assertLess(first_updated_at, ts.updated_at)
        sleep(0.05)
        ts.save()
        self.assertLess(first_updated_at, ts.updated_at)

    def test_to_dict(self):
        """To_dict method Test."""
        ts = BaseModel()
        self.assertIsInstance(ts.to_dict(), dict)
        self.assertIn("id", ts.to_dict())
        self.assertIn("created_at", ts.to_dict)
        self.assertIn("updated_at", ts.to_dict)
        self.assertin("__class__", ts.to_dict)

    def test_dunder_dict(self):
        """To_dict and __dict__ test comtrast."""
        ts = BaseModel()
        self.assertnotEqual(ts.to_dict(), ts.__dict__)


if __name__ == "__main__":
    unittest.main()
