from django.contrib import admin
from .models import Dating, Facilitator, Location, Facilitator

# Register your models here.

class DatingAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'location')
    list_filter = ('name', 'date')
    prepopulated_fields = {'friend_slug': ('name', )}

class LocationAdmin(admin.ModelAdmin):
    list_display = ('city', 'address')
    list_filter = ('city', 'address')


class FacilitatorAdmin(admin.ModelAdmin):
    list_display = ('email', )
    list_filter = ('email', )


admin.site.register(Dating, DatingAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Facilitator, FacilitatorAdmin)

