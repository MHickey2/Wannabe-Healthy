from django.contrib import admin
from .models import Profile
from django_summernote.admin import SummernoteModelAdmin

admin.site.register(Profile)


class PostAdmin(SummernoteModelAdmin):

    list_display = ('user', 'bio', 'profile_pic')
    search_fields = ['user']
    list_filter = ('user')
