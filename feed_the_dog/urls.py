from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import feed_the_dog.views as views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", views.index, name="index"),
    path("db/", views.db, name="db"),
    path("dogs/", views.dog_listing, name="dogs"),
    path("feed_the_dog/", views.feed_the_dog, name="feed_dog"),
]