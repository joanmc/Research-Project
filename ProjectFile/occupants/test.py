import time as tm
from dateutil.parser import parse
from .views import *
from django.test import TestCase
from django.test import Client
from .models import Modules, Groundtruth, Rooms, Timemodule, Wifilogdata, PercentagePredictions, EstimatePredictions
import datetime














class OccupantsViewsTestCase(TestCase):
    def test_basic_addition(self):
        """Test that the tests are executing"""
        self.assertEqual(1 + 1, 2)


    def test_homepage(self):
        """Test that the homepage is accessible"""
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)


    # def test_database(self):
    #     """Test that the database empty and is responding to queries"""
    #     testReturn = Rooms.objects.all()
    #     print('empty database', len(testReturn))
    #     print(testReturn)
    #     self.assertTrue(len(testReturn) == 0)


    def test_add_room(self):
        """Test that the database empty and is responding to queries"""
        respBefore = Rooms.objects.all()
        print('Before', respBefore, ': len', len(respBefore))

        Rooms.objects.create(
            room='B-005',
            building='CS',
            campus='DUBLIN',
            capacity=25
        )
        Rooms.objects.create(
            room='B-006',
            building='CS',
            campus='DUBLIN',
            capacity=50
        )
        Rooms.objects.create(
            room='B-009',
            building='CS',
            campus='DUBLIN',
            capacity=120
        )

        respAfter = Rooms.objects.all()
        print('After', respAfter, ': len', len(respAfter))
        self.assertTrue(len(respAfter) == 3)




    # def test_GenGraph(self):
    #     c = Client()
    #     c.login(username='', password='')
    #     # Extra parameters to make this a Ajax style request.
    #     kwargs = {'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'}
    #     url = '/GenGraph'
    #     data = {'timeModuleId': 236,}
    #     # csrf_client = Client(enforce_csrf_checks=True)
    #
    #     response = c.post(url, data, **kwargs)
    #     self.assertEqual(response.status_code, 200)



        # response = self.client.post(url, data, **kwargs)

        """ test needed that the query is in the database """


    # def test_calendarGen(self):
    #     """Test fails due to csrf not sent and query data not sent"""
    #     resp = self.client.post('/calendarGen')
    #     self.assertEqual(resp.status_code, 200)
    #
    # def test_RoomDayGraph(self):
    #     """Test fails due to csrf not sent and query data not sent"""
    #     resp = self.client.post('/RoomDayGraph')
    #     self.assertEqual(resp.status_code, 200)
    #
    # def test_register(self):
    #     """Test fails due to csrf not sent and query data not sent"""
    #     resp = self.client.post('/register/')
    #     self.assertEqual(resp.status_code, 200)
    #
    # def test_Rooms(self):
    #     """Test fails due to csrf not sent and query data not sent"""
    #     resp = self.client.post('/Rooms/')
    #     self.assertEqual(resp.status_code, 200)
    #
    # def test_Stats(self):
    #     """Test fails due to csrf not sent and query data not sent"""
    #     resp = self.client.post('/Stats/')
    #     self.assertEqual(resp.status_code, 200)





""" test that you can not access protected pages without logging in"""


def epochtime(x):
    """ rewrite as test """
    string = parse(x)
    epoch = int(tm.mktime(string.timetuple()))
    return epoch

print(epochtime("Wednesday, 27-Jul-16 11:37:51 GMT"))
