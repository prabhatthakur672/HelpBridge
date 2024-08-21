from django.contrib import admin

from .models import *

admin.site.register(HelpRequest)
admin.site.register(HelpOffer)
admin.site.register(Notification)
admin.site.register(RequestHistory)
admin.site.register(RequestView)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_no', 'bio', 'profile_image')

admin.site.register(Profile, ProfileAdmin)