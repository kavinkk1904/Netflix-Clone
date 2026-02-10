from django.contrib import admin
from .models import Validation, Movies

class memoAdmin(admin.ModelAdmin):
    list_display = ('Username', 'Email', 'Password')

admin.site.register(Validation)

admin.site.register(Movies)