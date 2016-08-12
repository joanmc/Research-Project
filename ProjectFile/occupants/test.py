import time as tm
from dateutil.parser import parse
from .views import *
from django.test import TestCase


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """Test that the tests are executing"""

        self.assertEqual(1 + 1, 2)


class OccupantsViewsTestCase(TestCase):
    def test_homepage(self):
        """Test that the homepage is accessible"""
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_GenGraph(self):
        """Test fails due to csrf not sent and query data not sent"""
        resp = self.client.post('/GenGraph')
        self.assertEqual(resp.status_code, 200)

    def test_calendarGen(self):
        """Test fails due to csrf not sent and query data not sent"""
        resp = self.client.post('/calendarGen')
        self.assertEqual(resp.status_code, 200)

    def test_RoomDayGraph(self):
        """Test fails due to csrf not sent and query data not sent"""
        resp = self.client.post('/RoomDayGraph')
        self.assertEqual(resp.status_code, 200)

    def test_register(self):
        """Test fails due to csrf not sent and query data not sent"""
        resp = self.client.post('/register/')
        self.assertEqual(resp.status_code, 200)

    def test_Rooms(self):
        """Test fails due to csrf not sent and query data not sent"""
        resp = self.client.post('/Rooms/')
        self.assertEqual(resp.status_code, 200)

    def test_Stats(self):
        """Test fails due to csrf not sent and query data not sent"""
        resp = self.client.post('/Stats/')
        self.assertEqual(resp.status_code, 200)





""" test that you can not access protected pages without logging in"""


def epochtime(x):
    """ rewrite as test """
    string = parse(x)
    epoch = int(tm.mktime(string.timetuple()))
    return epoch

print(epochtime("Wednesday, 27-Jul-16 11:37:51 GMT"))


def GenGraphTest(x):
    GenGraph()
    print('X')
