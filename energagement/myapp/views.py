from django.shortcuts import render_to_response
from django.shortcuts import render

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

    test1 = list(StreetLighting1.objects.all())
    return render(request,'myapp/main.html', {'test':test1})


def data_main(request):

    json_list=[]
    data=StreetLighting1.objects.all()[4:7]
    for item in data:
        json_item = {'type': "street_lighting1",
                     'dimos': item.municipality,
                     'kwdikos': item.code,
                     'latitude': item.latitude,
                     'longitude': item.longitude,
                    }
        print(item.latitude)
        json_list.append(json_item)
    data=Building.objects.all()
    for item in data:
        json_item = {'type': "building",
                     'dimos': item.municipality,
                     'kwdikos': item.building_code,
                     'latitude': item.latitude,
                     'longitude': item.longitude,
                    }
        print(item.latitude)
        json_list.append(json_item)
    data=StreetLighting.objects.all()
    for item in data:
        json_item = {'type': "street_lighting",
                     'dimos': item.municipality,
                     'kwdikos': item.line_code,
                     'latitude': item.latitude,
                     'longitude': item.longitude,
                    }
        print(item.latitude)
        json_list.append(json_item)
    data=ElectricVehicle.objects.all()
    for item in data:
        json_item = {'type': "EV",
                     'dimos': item.municipality,
                     'kwdikos': item.chargingpoint_code,
                     'latitude': item.latitude,
                     'longitude': item.longitude,
                    }
        print(item.latitude)
        json_list.append(json_item)
    return HttpResponse(json.dumps(json_list), content_type='application/json')


def buildings(request):

    all_buildings = list(Building.objects.all())
    return render(request, 'myapp/buildings.html', {'all_buildings': all_buildings},)


def data_buildings(request):
    ids = request.GET['state']
    indicator = request.GET['state2']
    time_scope = request.GET['state3']
    from_date = request.GET['state4']
    to_date = request.GET['state5']
    from_date1=datetime.strptime(from_date,"%Y-%m-%d").date()
    to_date1=datetime.strptime(to_date,"%Y-%m-%d").date()
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

        for id in list_of_ids:
            data1 = Building.objects.get(id=id)
            if indicator == "kwh" or indicator == "kwh_m2":
                list = data1.kwh.all()
            elif indicator == "lt" or indicator == "lt_m2":
                list = data1.lt.all()
            elif indicator == "kw":
                list = data1.kw.all()
            elif indicator == "co2_tn" or indicator == "co2_tn_m2":
                list = data1.co2_tn.all()
            elif indicator == "co2_lt" or indicator == "co2_lt_m2":
                list = data1.co2_lt.all()
            for item2 in list:
                 if item2.timestamp.strftime('%Y-%m-%d') >= from_date1.strftime('%Y-%m-%d') and item2.timestamp.strftime('%Y-%m-%d') <= to_date1.strftime('%Y-%m-%d'):
                     if time_scope=="month":
                         timestamp=item2.timestamp.strftime('%b')
                     elif time_scope=="week":
                         timestamp=(Week(int(item2.timestamp.strftime('%Y')),int(item2.timestamp.strftime('%W'))).monday()).strftime('%d-%m-%Y')+"  -  "+(Week(int(item2.timestamp.strftime('%Y')),int(item2.timestamp.strftime('%W'))).sunday()).strftime('%d-%m-%Y')
                     elif time_scope=="day":
                         timestamp=item2.timestamp.strftime('%d-%b')
                     else:
                         timestamp=item2.timestamp.strftime('%d-%b %H:%M:%S')
                     if indicator == "kwh" or indicator == "lt" or indicator == "kw" or indicator == "co2_tn" or indicator == "co2_lt":
                         metric=format(float(item2.metric),'.3f')
                     else:
                         metric=format(float(item2.metric)/data1.surface,'.3f')
                     json_item = {'municipality': data1.municipality,
                                  'code': data1.building_code,
                                  'metric': metric,
                                  'timestamp': timestamp}
                     json_list.append(json_item)
    return HttpResponse(json.dumps(json_list), content_type='application/json')

def street_lighting(request):

    all_street_lighting = list(StreetLighting.objects.all())
    return render_to_response('myapp/street_lighting.html', {'all_street_lighting': all_street_lighting},)

def data_street_lighting(request):
    ids = request.GET['state']
    indicator = request.GET['state2']
    time_scope = request.GET['state3']
    from_date = request.GET['state4']
    to_date = request.GET['state5']
    from_date1=datetime.strptime(from_date,"%Y-%m-%d").date()
    to_date1=datetime.strptime(to_date,"%Y-%m-%d").date()
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

        for id in list_of_ids:
            data1 = StreetLighting.objects.get(id=id)
            if indicator == "kwh" or indicator == "kwh_line_length" or indicator == "kwh_light":
                list = data1.kwh.all()
            elif indicator == "kw":
                list = data1.kw.all()
            elif indicator == "co2_tn" or indicator == "co2_tn_line_length":
                list = data1.co2_tn.all()
            for item2 in list:
                 if item2.timestamp.strftime('%Y-%m-%d') >= from_date1.strftime('%Y-%m-%d') and item2.timestamp.strftime('%Y-%m-%d') <= to_date1.strftime('%Y-%m-%d'):
                     if time_scope=="month":
                         timestamp=item2.timestamp.strftime('%b')
                     elif time_scope=="week":
                         timestamp=(Week(int(item2.timestamp.strftime('%Y')),int(item2.timestamp.strftime('%W'))).monday()).strftime('%d-%m-%Y')+"  -  "+(Week(int(item2.timestamp.strftime('%Y')),int(item2.timestamp.strftime('%W'))).sunday()).strftime('%d-%m-%Y')
                     elif time_scope=="day":
                         timestamp=item2.timestamp.strftime('%d-%b')
                     else:
                         timestamp=item2.timestamp.strftime('%d-%b %H:%M:%S')
                     if indicator == "kwh" or indicator == "kw" or indicator == "co2_tn":
                         metric=format(float(item2.metric),'.3f')
                     elif indicator == "kwh_light":
                         metric=format(float(item2.metric)/data1.lights_number,'.3f')
                     else:
                         metric=format(float(item2.metric)/data1.line_length,'.3f')
                     json_item = {'municipality': data1.municipality,
                                  'code': data1.line_code,
                                  'metric': metric,
                                  'timestamp': timestamp}
                     json_list.append(json_item)
    return HttpResponse(json.dumps(json_list), content_type='application/json')

def EVs(request):

    all_EVs = list(ElectricVehicle.objects.all())
    return render_to_response('myapp/EVs.html',  {'all_EVs': all_EVs},)


def data_EVs(request):

    ids = request.GET['state']
    indicator = request.GET['state2']
    time_scope = request.GET['state3']
    from_date = request.GET['state4']
    to_date = request.GET['state5']
    from_date1=datetime.strptime(from_date,"%Y-%m-%d").date()
    to_date1=datetime.strptime(to_date,"%Y-%m-%d").date()
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

        for id in list_of_ids:
            data1 = ElectricVehicle.objects.get(id=id)
            if indicator == "kwh":
                list = data1.kwh.all()
            elif indicator == "total_charging_points":
                list = data1.total_charging_points.all()
            elif indicator == "available_charging_points":
                list = data1.available_charging_points.all()
            elif indicator == "co2_tn":
                list = data1.co2_tn.all()
            for item2 in list:
                 if item2.timestamp.strftime('%Y-%m-%d') >= from_date1.strftime('%Y-%m-%d') and item2.timestamp.strftime('%Y-%m-%d') <= to_date1.strftime('%Y-%m-%d'):
                     if time_scope=="month":
                         timestamp=item2.timestamp.strftime('%b')
                     elif time_scope=="week":
                         timestamp=(Week(int(item2.timestamp.strftime('%Y')),int(item2.timestamp.strftime('%W'))).monday()).strftime('%d-%m-%Y')+"  -  "+(Week(int(item2.timestamp.strftime('%Y')),int(item2.timestamp.strftime('%W'))).sunday()).strftime('%d-%m-%Y')
                     elif time_scope=="day":
                         timestamp=item2.timestamp.strftime('%d-%b')
                     else:
                         timestamp=item2.timestamp.strftime('%d-%b %H:%M:%S')
                     if indicator == "kwh" or indicator == "co2_tn":
                         metric=format(float(item2.metric),'.3f')
                     else:
                         metric=item2.metric
                     json_item = {'municipality': data1.municipality,
                                  'code': data1.chargingpoint_code,
                                  'metric': metric,
                                  'timestamp': timestamp}
                     json_list.append(json_item)
    return HttpResponse(json.dumps(json_list), content_type='application/json')


#def test2(request):

  #  return render_to_response('myapp/test2.html')


def mydata(request):
    test1 = list(StreetLighting1.objects.all())
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