from django.test import TestCase
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Modules
from .models import Rooms
from .models import Timemodule
from .models import Wifilogdata
from django.db.models import Q
from datetime import timedelta, date
import datetime
from django.http import HttpResponse




# Create your tests here.


def test():

    start_time = datetime.date(2015, 11, 2)
    dates = Wifilogdata.objects.filter(room = 'B003', datetime__day = start_time)
    print("working")


test()




def test(request):

    if request.is_ajax():

        start_time = datetime.datetime(2015, 11, 3, 11, 00)
        dateX = Wifilogdata.objects.filter(datetime__range=(start_time, start_time + timedelta(hours = 1)))
##        dateX = Wifilogdata.objects.get(wifilogdataid  = 327)
        listx =  []

        for x in dateX:
            print(x.room.capacity)
            print(x.datetime)
            print(x.authenticated)
            
            if not listx: 
                listx.append(x.authenticated)
            listx.append(', ')
            listx.append(x.authenticated)
        dates = 'workingX'
        print(listx)
        return HttpResponse(listx)
##        return render_to_response('occupants/homepage.html', {'listx': listx}, context_instance=RequestContext(request))
##        return render_to_response('occupants/homepage.html', {'dates': dates})

    else:
    	raise Http404




        $(document).ready(function() {
            var theVar = 5;
            $("button").click(function(){
                $.ajax({
                    method: "POST",
                    data: {'theVar': theVar, csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,},
                    url: "/test",
                    success: function(result) {
                        var graphData = result;
                        var graphInformation = graphData[2];
                        document.getElementById('testDiv').innerHTML = graphInformation;
                }})
            });
        });



    </script>
        $.jqplot('div_report', [xy]),
        { title:'Exponential Line', axes:{min:-10, max:240}}, lengend:{ labels: ['UI Tutorial Data'], renderer: $jqplot.EhancedLegendRenderer, show:true}, series:[{color:'#5FAB78'}]
    <script>


        $(document).ready(function(){
           var plot1 = $.jqplot ('graphDiv', [[3,7,9,1,5,3,8,2,5]]);
        });



