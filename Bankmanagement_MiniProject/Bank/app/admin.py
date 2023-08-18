from django.contrib import admin

from .models import OpenAccount, Status

# Register your models here.

admin.site.register(OpenAccount)
admin.site.register(Status)