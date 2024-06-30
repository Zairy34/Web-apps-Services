from django.contrib import admin
from .models import MainServices, OUR_TECHNICIANS, Clients_reviews,ServiceRequest,ALLServices

admin.site.register(ServiceRequest)


@admin.register(MainServices)
class MainServicesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image')



@admin.register(OUR_TECHNICIANS)
class OUR_TECHNICIANSAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image')

@admin.register(Clients_reviews)
class Clients_reviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'reviews', 'image')
    
    
@admin.register(ALLServices)
class ALLServicesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image')