from collections import defaultdict

from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting, Dog

# Create your views here.
def index(request):

    print(request)
    return render(request, "index.html")



def db(request):
    greeting = Greeting()

    if not request.user.is_anonymous:
        greeting.who = request.user

    greeting.where = request.META.get("REMOTE_ADDR", "unknown")

    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})

def dog_listing(request):

    dogs = Dog.objects.all().values_list('name', 'owners__username')
    ownership_dict = dict()
    for dog_name, owner_username in dogs:
        if dog_name not in ownership_dict:
            ownership_dict[dog_name] = list()
        ownership_dict[dog_name].append(owner_username)

    return render(request, "dog_list.html", {"dog_ownership_dict": ownership_dict})



