from django.contrib import admin
from .models import Groundtruth, Modules, Rooms, Timemodule, Wifilogdata


admin.site.register(Groundtruth)
admin.site.register(Modules)
admin.site.register(Rooms)
admin.site.register(Timemodule)
admin.site.register(Wifilogdata)
