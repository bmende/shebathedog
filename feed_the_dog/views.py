from collections import defaultdict

from datetime import datetime, timedelta, timezone

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User

from .models import Greeting, Dog, Feeding

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

    dogs = Dog.objects.all().values_list('name', 'owners__first_name')
    ownership_dict = dict()
    for dog_name, owner_firstname in dogs:
        if dog_name not in ownership_dict:
            ownership_dict[dog_name] = list()
        ownership_dict[dog_name].append(owner_firstname)

    return render(request, "dog_list.html", {"dog_ownership_dict": ownership_dict})

def feed_the_dog(request):

    who = request.user
    if who.is_anonymous:
        return HttpResponseRedirect("/")

    dogs = Dog.objects.filter(owners__in=[who])

    if request.method == 'POST':
        for dog in dogs:
            latest_feeding = Feeding(feeder=who, dog=dog)
            latest_feeding.save()

    feeds = Feeding.objects.filter(dog__in=dogs).values().order_by("-when")

    now = datetime.now(timezone.utc)

    if feeds:
        last_fed = feeds[0].get('when')
        last_feeder = User.objects.get(pk=feeds[0].get('feeder_id')).first_name
    else:
        last_fed = now - timedelta(hours=12)
        last_feeder = who.first_name

    disable_feed = False
    if now - last_fed < timedelta(hours=1):
        feed_class = "success"
        disable_feed = True
    elif now - last_fed < timedelta(hours=5):
        feed_class = "success"
    elif now - last_fed < timedelta(hours=12):
        feed_class = "warning"
    else:
        feed_class = "danger"

    dog_names = ", ".join(list(dogs.values_list("name", flat=True)))

    if not feeds:
        last_fed = None

    data_dict = {"feed_class": feed_class,
                 "last_fed": last_fed,
                 "last_feeder": last_feeder,
                 "dogs": dog_names,
                 "disable_feed": disable_feed}

    return render(request, "dog_feeding.html", data_dict)




