from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'sex', 'img', 'agreement')
    list_display_links = ('user',)


admin.site.register(Profile, ProfileAdmin)
