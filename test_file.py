from .ProjectFile.occupants.models import Timemodule
from django.utils import timezone
from django.shortcuts import render
from django.db.models import Q
import datetime

start_time = datetime.date(2015, 11, 1)
end_time = datetime.date(2015, 11, 7)

'''start_time = timezone.make_aware(start_time, timezone.get_current_timezone())
'''

x = Timemodule.objects.filter(room='B-003', datetime__range=(start_time, end_time))


for z in y:
    print(z.room.room, z.datetime.date, z.module)
