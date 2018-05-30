from django.contrib import admin
from .models import Owner, Dog, Walk

admin.site.register([Owner, Dog, Walk])

