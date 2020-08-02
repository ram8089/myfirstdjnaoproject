from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from meetings.models import Meeting
# Create your views here.
def welcome(request):
    return render(request, "wesite1/welcome.html", {"message": "this is my fist parameter passed", "y": Meeting.objects.all()})

def about(request):
    return HttpResponse("heY THIS IS RAM")