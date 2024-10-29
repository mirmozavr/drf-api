from django.contrib import admin

from .models import People, Category
# Register your models here.

admin.site.register(People)
admin.site.register(Category)