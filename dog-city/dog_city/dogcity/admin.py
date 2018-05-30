from django.contrib import admin
from .models import Owner, Dog, Playdate

admin.site.register([Owner, Dog, Playdate])

