#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ """
        self.value.place_id = "d54asda-d45asw-da45w"
        self.assertEqual(type(self.value.place_id), str)

    def test_user_id(self):
        """ """
        self.value.user_id = "e45qw4-d2as1w5"
        self.assertEqual(type(self.value.user_id), str)

    def test_text(self):
        """ """
        self.value.text = "Great place"
        self.assertEqual(type(self.value.text), str)
