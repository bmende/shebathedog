from django.contrib import admin
from hello.models import Greeting, Dog, Ownership

# Register your models here.
admin.site.register(Greeting)
admin.site.register(Dog)
admin.site.register(Ownership)