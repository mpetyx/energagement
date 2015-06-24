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
from .models import StreetLighting
from django.http import HttpResponse
import json

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

def EV(request):

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

        return render(request, 'myapp/EV.html', {'EV_':EV_,'form1':form1,'form2':form2,'form3':form3,'form4':form4,'form5':form5,'form6':form6, 'choose_time':choose_time, 'diagram':diagram, 'test':test},)
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
        return render(request, 'myapp/EV.html', {'EV_':EV_,'form1':form1, 'form2':form2, 'form3':form3,'form4':form4,'form5':form5,'form6':form6,'choose_time':choose_time,'diagram':diagram, 'test':test},)



def test(request):

    return render_to_response('myapp/test.html')

def test2(request):

    return render_to_response('myapp/test2.html')

def aggelos(request):
    return render(request, 'myapp/aggelos.html', {})

def aggelos_data(request):
    status = request.GET['state']
    data = StreetLighting.objects.all()
    if status == "true":
        json_list = []
        for item in data:
            json_item = {'dimos': item.municipality,
                         'kwdikos': item.code
            }
            json_list.append(json_item)
    else:
        json_list = [
            {'karekla': 'Aggelou', 'upsos':5},
            {'karekla':"Vasilikis", "upsos": 2}
        ]
    return HttpResponse(json.dumps(json_list), content_type='application/json')