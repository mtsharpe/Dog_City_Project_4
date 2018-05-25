from django.contrib import admin
from .models import Owner, Dog, Playdate, Attendance

admin.site.register([Owner, Dog, Playdate, Attendance])

