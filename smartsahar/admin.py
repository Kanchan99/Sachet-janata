from django.contrib import admin
from .models import City,Events

# Register your models here.
@admin.register(City)
class CityAdmin(admin.ModelAdmin):
	list_display=('name','state','governor')

@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
	list_display=('event','posted_by','citizensip_no','posted_on')

