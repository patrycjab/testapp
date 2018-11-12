from django.contrib import admin

# Register your models here.

from .models import Email, Statistic

admin.site.register(Email)
admin.site.register(Statistic)
