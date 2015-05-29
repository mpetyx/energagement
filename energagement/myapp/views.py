from django.shortcuts import render_to_response
from django.shortcuts import render
from .forms import myForm

def main(request):

    return render_to_response('myapp/main.html')

def buildings(request):

    return render_to_response('myapp/buildings.html')

def street_lighting(request):

    return render_to_response('myapp/street_lighting.html')

def EV(request):

    form=myForm()
    return render(request, 'myapp/EV.html', {'form':form},)

def test(request):

    return render_to_response('myapp/test.html')

