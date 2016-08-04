import time as tm
from dateutil.parser import parse


def epochtime(x):
    string = parse(x)
    epoch = int(tm.mktime(string.timetuple()))
    return epoch


print(epochtime("Wednesday, 27-Jul-16 11:37:51 GMT"))