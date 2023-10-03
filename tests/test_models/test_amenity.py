#!/usr/bin/python3
""" Test case for Amenity class """
from tests.test_models.test_base_model import TestBasemodel
from models.amenity import Amenity
from models import st_type


class TestAmenity(TestBasemodel):
    """ amenity test class"""

    def __init__(self, *args, **kwargs):
        """inti the test class """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """testing name type """
        new = self.value()
        self.assertEqual(type(new.name), str if
                         st_type != 'db' else
                         type(None))
