from django.contrib import admin
from feed_the_dog.models import Greeting, Dog


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    fields = ('name', 'owners')
    list_display = ('name', 'owner_names')

    def owner_names(self, obj):
        print(list(obj.owners.values_list('first_name')))
        return ", ".join(str(name[0]) for name in obj.owners.values_list('first_name'))

@admin.register(Greeting)
class GreetingAdmin(admin.ModelAdmin):
    readonly_fields = ('when', 'who', 'where')
    date_hierarchy = 'when'
    list_display = ('when', 'who', 'where')
