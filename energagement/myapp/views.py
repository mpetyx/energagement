from django.shortcuts import render_to_response
from django.shortcuts import render
from .forms import myForm1
from .forms import myForm2
from .forms import myForm3
from .forms import myForm4
from .forms import myForm5
from .forms import myForm6

from .forms import my_choose_time
from .forms import my_EV
from .models import *
from django.http import HttpResponse
import json
from datetime import datetime
from datetime import date, timedelta
from datetime import time
from django.http import HttpResponseRedirect
import cgi
from isoweek import Week

def get_week_days(year, week):
    d = date(year,1,1)
    if(d.weekday()>3):
        d = d+timedelta(7-d.weekday())
    else:
        d = d - timedelta(d.weekday())
    dlt = timedelta(days = (week-1)*7)
    return d + dlt,  d + dlt + timedelta(days=6)

def home(request):

    return render_to_response('myapp/home.html')


def main(request):

    return render_to_response('myapp/main.html')


def buildings(request):

    return render_to_response('myapp/buildings.html')


def street_lighting(request):

    return render_to_response('myapp/street_lighting.html')


def EV(request):

    return render_to_response('myapp/EV.html')


def test(request):

    return render_to_response('myapp/test.html')


#def test2(request):

  #  return render_to_response('myapp/test2.html')


def mydata(request):
    test1 = list(StreetLighting1.objects.all())
    #current_date = date.today()
    return render(request, 'myapp/mydata.html', {'test1': test1},)

def data_test(request):

    ids = request.GET['state']
    indicator = request.GET['state2']
    time_scope = request.GET['state3']
    from_date = request.GET['state4']
    to_date = request.GET['state5']
    #print (from_date)
    #print (to_date)
    from_date1=datetime.strptime(from_date,"%Y-%m-%d").date()
    to_date1=datetime.strptime(to_date,"%Y-%m-%d").date()
    print (from_date1)
    print (to_date1)
    # seperate graph-button-ids
    if ids=="":
        json_list=[]
    else:
        button_list = ids.split("_")
        list_of_ids = []
        for b in button_list:
            # hold only the ids
            list_of_ids.append(int(b.split('graph-button-')[1]))
        print ("list of ids=", list_of_ids)
        json_list=[]
        if indicator=="kw":
            for id in list_of_ids:
                data1=StreetLighting1.objects.get(id=id)
                kw = data1.kw.all()
                #kw = data1.kw.get(timestamp=)
                for item2 in kw:
                    print ("item2=", item2.timestamp.strftime('%Y-%m-%d'))
                    #print (item2.timestamp.strftime('%W'))
                    print (Week(int(item2.timestamp.strftime('%Y')),int(item2.timestamp.strftime('%W'))).monday())
                    if item2.timestamp.strftime('%Y-%m-%d') >= from_date1.strftime('%Y-%m-%d') and item2.timestamp.strftime('%Y-%m-%d') <= to_date1.strftime('%Y-%m-%d'):
                        #print(item2.timestamp.month)
                        #print(datetime.now().month)
                        if time_scope=="month":
                            json_item = {'dimos': data1.municipality,
                                         'kwdikos': data1.code,
                                         'metric': item2.metric,
                                         'timestamp': item2.timestamp.strftime('%b')}
                            print(item2.metric)
                            json_list.append(json_item)
                        elif time_scope=="week":
                            json_item = {'dimos': data1.municipality,
                                         'kwdikos': data1.code,
                                         'metric': item2.metric,
                                        # 'timestamp': item2.timestamp.strftime('%A')
                                         'timestamp': (Week(int(item2.timestamp.strftime('%Y')),int(item2.timestamp.strftime('%W'))).monday()).strftime('%d-%m-%Y')+"  -  "+(Week(int(item2.timestamp.strftime('%Y')),int(item2.timestamp.strftime('%W'))).sunday()).strftime('%d-%m-%Y')}
                            print(item2.metric)
                            json_list.append(json_item)
                        elif time_scope=="day":
                            json_item = {'dimos': data1.municipality,
                                         'kwdikos': data1.code,
                                         'metric': item2.metric,
                                         'timestamp': item2.timestamp.strftime('%d-%b')}
                            print(item2.metric)
                            json_list.append(json_item)
                        else:
                            json_item = {'dimos': data1.municipality,
                                         'kwdikos': data1.code,
                                         'metric': item2.metric,
                                         'timestamp': item2.timestamp.strftime('%d-%b %H:%M:%S')}
                            print(item2.metric)
                            json_list.append(json_item)
        elif indicator=="kwh":
            for id in list_of_ids:
                data1=StreetLighting1.objects.get(id=id)
                kwh = data1.kwh.all()
                for item2 in kwh:
                    json_item = {'dimos': data1.municipality,
                                 'kwdikos': data1.code,
                                 'metric': item2.metric,
                                 'timestamp': item2.timestamp.strftime('%d-%b-%Y %H:%M:%S')}
                    print(item2.metric)
                    json_list.append(json_item)

    return HttpResponse(json.dumps(json_list), content_type='application/json')