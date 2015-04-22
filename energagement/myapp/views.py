from django.shortcuts import render_to_response

def main(request):

    return render_to_response('myapp/main.html')