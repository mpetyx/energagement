from django.shortcuts import render_to_response
from django.shortcuts import render
from .forms import myForm
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
        form = myForm(request.GET)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')
        return render(request, 'myapp/EV.html', {'form':form, 'diagram':diagram})
    #form=myForm()
    # if a GET (or any other method) we'll create a blank form
    else:
        # form1 = cgi.FieldStorage()
        # diagram = form1.getvalue('diagram')
        diagram = request.POST.get("diagram","")
        form = myForm()
        return render(request, 'myapp/EV.html', {'form':form, 'diagram':diagram},)


def test(request):

    return render_to_response('myapp/test.html')

