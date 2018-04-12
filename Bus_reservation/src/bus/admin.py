from django.contrib import admin
from .models import Bus,Stop

# Register your models here.
class BusAdmin(admin.ModelAdmin):
    #sets up values for how admin site lists categories
    list_display = ('bus_number', 'created_at', 'updated_at',)
    list_display_links = ('bus_number',)
    list_per_page = 20
    ordering = ['bus_number']
    search_fields = ['bus_number', 'arriving_from', 'depature_at']
    exclude = ('created_at', 'updated_at',)
    # sets up slug to be generated from category name
    prepopulated_fields = {'slug' : ('bus_number',)}

admin.site.register(Bus, BusAdmin)

class StopAdmin(admin.ModelAdmin):
    #sets up values for how admin site lists categories
    list_display = ('area_name', 'created_at', 'updated_at',)
    list_display_links = ('area_name',)
    list_per_page = 20
    ordering = ['area_name']
    search_fields = ['area_name']
    exclude = ('created_at', 'updated_at',)

    # sets up slug to be generated from category name
    prepopulated_fields = {'slug' : ('area_name',)}

admin.site.register(Stop, StopAdmin)
#
# class BusDropAreaAdmin(admin.ModelAdmin):
#     #sets up values for how admin site lists categories
#     list_display = ('area_name', 'created_at', 'updated_at',)
#     list_display_links = ('area_name',)
#     list_per_page = 20
#     ordering = ['area_name']
#     search_fields = ['area_name']
#     exclude = ('created_at', 'updated_at',)
#
#     # sets up slug to be generated from category name
#     prepopulated_fields = {'slug' : ('area_name',)}

# admin.site.register(BusDropArea, BusDropAreaAdmin)
