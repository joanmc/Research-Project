import time as tm
from dateutil.parser import parse
from .views import *


def epochtime(x):
    string = parse(x)
    epoch = int(tm.mktime(string.timetuple()))
    return epoch

print(epochtime("Wednesday, 27-Jul-16 11:37:51 GMT"))


# def GenGraphTest(x):
#     GenGraph()
#     print('X')
