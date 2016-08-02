from django.contrib import admin
from .models import Rooms, Modules, Timemodule, Wifilogdata, Groundtruth, BinaryPredictions, EstimatePredictions, PercentagePredictions


admin.site.register(Groundtruth)
admin.site.register(Modules)
admin.site.register(Rooms)
admin.site.register(Timemodule)
admin.site.register(Wifilogdata)
admin.site.register(BinaryPredictions)
admin.site.register(PercentagePredictions)
admin.site.register(EstimatePredictions)

