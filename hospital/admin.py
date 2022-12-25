from django.contrib import admin
from .models import Hospital,Departments,Staff

# Register your models here.

admin.site.register([Hospital,Departments,Staff])