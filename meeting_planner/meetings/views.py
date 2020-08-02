from django.shortcuts import render,get_object_or_404
from .models import Meeting, Rooms

# Create your views here.
def detail(request,id):
    #meeting = Meeting.objects.get(pk=id)
    #this is to show error 404
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})
def room_list(request):
    return render(request, "meetings/rooms_list.html", {"rooms": Rooms.objects.all()})