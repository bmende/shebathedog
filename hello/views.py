from collections import defaultdict

from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting, Dog, Ownership

# Create your views here.
def index(request):

    print(request)
    return render(request, "index.html")



def db(request):
    greeting = Greeting()

    if request.user is not None:
        greeting.who = request.user
    else:
        greeting.who = "anonymous"

    greeting.where = request.META.get("REMOTE_ADDR", "unknown")


    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})

def dog_listing(request):

    owners_list = Ownership.objects.all().values_list("dog__name", "owner__first_name")


    ownership_dict = dict()
    for dog, name in owners_list:
        if not ownership_dict.get(dog, False):
            ownership_dict[dog] = list()
        ownership_dict[dog].append(name)


    return render(request, "dog_list.html", {"dog_ownership_dict": ownership_dict})



