from django.contrib import admin
from feed_the_dog.models import Greeting, Dog, Feeding


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    fields = ('name', 'owners')
    list_display = ('name', 'owner_names')

    def owner_names(self, obj):
        return ", ".join(str(name[0]) for name in obj.owners.values_list('first_name'))

@admin.register(Greeting)
class GreetingAdmin(admin.ModelAdmin):
    readonly_fields = ('when', 'who', 'where')
    date_hierarchy = 'when'
    list_display = ('when', 'who', 'where')

@admin.register(Feeding)
class FeedingAdmin(admin.ModelAdmin):
    readonly_fields = ('when', 'dog_name', 'feeder')
    date_hierarchy = 'when'
    list_display = ('when', 'dog_name', 'feeder')

    def dog_name(self, obj):
        return obj.dog.name
