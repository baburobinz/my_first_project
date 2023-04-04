from django.contrib import admin
from .models import user_details,booking_details,admin_details,gallery,offers,quotes

@admin.register(user_details)

class itemAdmin(admin.ModelAdmin):
    readonly_fields = ['user_name','password']

admin.site.register(booking_details)

admin.site.register(admin_details)

admin.site.register(gallery)

admin.site.register(offers)

admin.site.register(quotes)




