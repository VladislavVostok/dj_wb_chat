from django.shortcuts import render
from .models import Room,Message
from django.http import HttpResponse
from django.views.decorators.http import require_GET
from .utils import robots_txt_content



def index(request):
    return render(request, "index.html", {})

def rooms(request):
    rooms=Room.objects.all()
    context = {"rooms":rooms}
    return render(request, "rooms.html", context)

def room(request, slug):
    room_name=Room.objects.get(slug=slug).name
    messages=Message.objects.filter(room=Room.objects.get(slug=slug))
    context = {"room_name":room_name,"slug":slug,'messages':messages}
    return render(request, "room.html", context)

@require_GET
def robots_txt(request):
    return HttpResponse(robots_txt_content, content_type="text/plain")

