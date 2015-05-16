from django.shortcuts import render_to_response

def main(request):

    return render_to_response('myapp/main.html')

def buildings(request):

    return render_to_response('myapp/buildings.html')

def street_lighting(request):

    return render_to_response('myapp/street_lighting.html')

def EV(request):

    return render_to_response('myapp/EV.html')