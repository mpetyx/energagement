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

from django.http import HttpResponseRedirect
import cgi


def home(request):

    return render_to_response('myapp/home.html')


def main(request):

    return render_to_response('myapp/main.html')


def buildings(request):

    return render_to_response('myapp/buildings.html')


def street_lighting(request):

    return render_to_response('myapp/street_lighting.html')

"""def EV(request):

    if request.method == 'GET':
        diagram = None
        # create a form instance and populate it with data from the request:
        form1 = myForm1(request.GET)
        form2 = myForm2(request.GET)
        form3 = myForm3(request.GET)
        form4 = myForm4(request.GET)
        form5 = myForm5(request.GET)
        form6 = myForm6(request.GET)
       # form = UnknownForm(request.POST)

        choose_time = my_choose_time(request.GET)
        EV_ = my_EV(request.GET)
        # check whether it's valid:
        #if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
          #  return HttpResponseRedirect('/thanks/')
        test=list(StreetLighting.objects.all())

        return render(request, 'myapp/EV.html', {'EV_':EV_,'form1':form1,'form2':form2,'form3':form3,'form4':form4,
        'form5':form5,'form6':form6, 'choose_time':choose_time, 'diagram':diagram, 'test':test},)
    #form=myForm()
    # if a GET (or any other method) we'll create a blank form
    else:
        # form1 = cgi.FieldStorage()
        # diagram = form1.getvalue('diagram')
        diagram = request.POST.get("diagram","")
        form1 = myForm1()
        form2 = myForm2()
        form3 = myForm3()
        form4 = myForm4()
        form5 = myForm5()
        form6 = myForm6()
        choose_time = my_choose_time()
       # form = UnknownForm(request.POST)
        EV_ = my_EV()

        test=list(StreetLighting.objects.all())
        return render(request, 'myapp/EV.html', {'EV_':EV_,'form1':form1, 'form2':form2, 'form3':form3,
        'form4':form4,'form5':form5,'form6':form6,'choose_time':choose_time,'diagram':diagram, 'test':test},)
"""

def EV(request):

    return render_to_response('myapp/EV.html')


def test(request):

    return render_to_response('myapp/test.html')


#def test2(request):

  #  return render_to_response('myapp/test2.html')


def mydata(request):
    test1 = list(StreetLighting1.objects.all())
    return render(request, 'myapp/mydata.html', {'test1': test1},)

def data_kwh(request):

    status = request.GET['state_kwh']
   # status2 = request.GET['state2']

    #data = StreetLighting.objects.get()

    if status == "true":
        json_list = []
        data1 = StreetLighting1.objects.get(id=1)
        #for item in data1:
        kwh = data1.kwh.all()
        for item2 in kwh:
            json_item = {'dimos': data1.municipality,
                         'kwdikos': data1.code,
                         'metric': item2.metric,
                         'timestamp': item2.timestamp.strftime('%d-%b-%Y %H:%M:%S')}
            json_list.append(json_item)
    else:
        json_list = []

    return HttpResponse(json.dumps(json_list), content_type='application/json')

def data_kwh2(request):

    status = request.GET['state_kw2']
   # status2 = request.GET['state2']

    #data = StreetLighting.objects.get()

    if status == "true":
        json_list = []
        data1 = StreetLighting1.objects.get(id=2)
        #for item in data1:
        kwh = data1.kwh.all()
        for item2 in kwh:
            json_item = {'dimos': data1.municipality,
                         'kwdikos': data1.code,
                         'metric': item2.metric,
                         'timestamp': item2.timestamp.strftime('%d-%b-%Y %H:%M:%S')}
            json_list.append(json_item)
    else:
        json_list = []

    return HttpResponse(json.dumps(json_list), content_type='application/json')

def data_kwh1_2(request):

    status = request.GET['state_kwh1_2']
   # status2 = request.GET['state2']

    #data = StreetLighting.objects.get()

    if status == "true":
        json_list = []
        data1 = StreetLighting1.objects.get(id=1)
        #for item in data1:
        kwh = data1.kwh.all()
        for item2 in kwh:
            json_item = {'dimos': data1.municipality,
                         'kwdikos': data1.code,
                         'metric': item2.metric,
                         'timestamp': item2.timestamp.strftime('%d-%b-%Y %H:%M:%S')}
            json_list.append(json_item)
        data1 = StreetLighting1.objects.get(id=2)
        #for item in data1:
        kwh = data1.kwh.all()
        for item2 in kwh:
            json_item = {'dimos': data1.municipality,
                         'kwdikos': data1.code,
                         'metric': item2.metric,
                         'timestamp': item2.timestamp.strftime('%d-%b-%Y %H:%M:%S')}
            json_list.append(json_item)
    else:
        json_list = []

    return HttpResponse(json.dumps(json_list), content_type='application/json')

def data_test(request):

    status = request.GET['state']
    status2 = request.GET['state2']
    print (status2)
    # seperate graph-button-ids
    button_list = status.split("_")
    list_of_ids = []
    for b in button_list:
        # hold only the ids
        list_of_ids.append(int(b.split('graph-button-')[1]))
    print ("list of ids=", list_of_ids)
    json_list=[]
    if status2=="kw":
        for id in list_of_ids:
            data1=StreetLighting1.objects.get(id=id)
            kw = data1.kw.all()
            for item2 in kw:
                json_item = {'dimos': data1.municipality,
                             'kwdikos': data1.code,
                             'metric': item2.metric,
                             'timestamp': item2.timestamp.strftime('%d-%b-%Y %H:%M:%S')}
                print(item2.metric)
                json_list.append(json_item)
    elif status2=="kwh":
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

def data_test2(request):

    status2 = request.GET['state2']

    #data = StreetLighting.objects.get()

    if status2 == "true":
        json_list = []
        data1 = StreetLighting1.objects.get(id=2)
        #for item in data1:
        kw = data1.kw.all()
        for item2 in kw:
            json_item = {'dimos': data1.municipality,
                         'kwdikos': data1.code,
                         'metric': item2.metric,
                         'timestamp': item2.timestamp.strftime('%d-%b-%Y %H:%M:%S')}
            json_list.append(json_item)

    else:
        json_list = []

    return HttpResponse(json.dumps(json_list), content_type='application/json')


def data_test1_2(request):

    status1_2 = request.GET['state1_2']

    #data = StreetLighting.objects.get()

    if status1_2 == "true":
        json_list = []
        data1 = StreetLighting1.objects.get(id=1)
        #for item in data1:
        kw = data1.kw.all()
        for item2 in kw:
            json_item = {'dimos': data1.municipality,
                         'kwdikos': data1.code,
                         'metric': item2.metric,
                         'timestamp': item2.timestamp.strftime('%d-%b-%Y %H:%M:%S')}
            json_list.append(json_item)
        data1 = StreetLighting1.objects.get(id=2)
        #for item in data1:
        kw = data1.kw.all()
        for item2 in kw:
            json_item = {'dimos': data1.municipality,
                         'kwdikos': data1.code,
                         'metric': item2.metric,
                         'timestamp': item2.timestamp.strftime('%d-%b-%Y %H:%M:%S')}
            json_list.append(json_item)

    else:
        json_list = []

    return HttpResponse(json.dumps(json_list), content_type='application/json')