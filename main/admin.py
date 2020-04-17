from django.contrib import admin
from .models import Event, Email, Gal, Contact


# Register your models here.
admin.site.register(Event)
admin.site.register(Email)
admin.site.register(Contact)


 


class GalAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.save()
 
        for afile in request.FILES.getlist('photos_multiple'):
            Gal(img = afile).save()
 
admin.site.register(Gal, GalAdmin)