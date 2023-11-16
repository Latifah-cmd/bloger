from django.contrib import admin
from .models import Authour, Article

class AuthourAdmin(admin.ModelAdmin):
    list_display = ("name","gender","contact","address")

admin.site.register(Authour, AuthourAdmin)
