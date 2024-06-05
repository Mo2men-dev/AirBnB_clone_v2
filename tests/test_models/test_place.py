#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ """
        self.value.city_id = "re54wre-rwe5r74"
        self.assertEqual(type(self.value.city_id), str)

    def test_user_id(self):
        """ """
        self.value.user_id = "re54wre-rwe5r74"
        self.assertEqual(type(self.value.user_id), str)

    def test_name(self):
        """ """
        self.value.name = "Ali"
        self.assertEqual(type(self.value.name), str)

    def test_description(self):
        """ """
        self.value.description = "Good"
        self.assertEqual(type(self.value.description), str)

    def test_number_rooms(self):
        """ """
        self.value.number_rooms = 5
        self.assertEqual(type(self.value.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        self.value.number_bathrooms = 3
        self.assertEqual(type(self.value.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        self.value.max_guest = 15
        self.assertEqual(type(self.value.max_guest), int)

    def test_price_by_night(self):
        """ """
        self.value.price_by_night = 95
        self.assertEqual(type(self.value.price_by_night), int)

    def test_latitude(self):
        """ """
        self.value.latitude = 1.5
        self.assertEqual(type(self.value.latitude), float)

    def test_longitude(self):
        """ """
        self.value.longitude = 8.6
        self.assertEqual(type(self.value.longitude), float)
