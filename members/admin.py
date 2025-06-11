from django.contrib import admin

from .models import MembersModel, Category 
admin.site.register(MembersModel)
admin.site.register(Category)
