from django.contrib import admin
from .models import Employee,Registration,Fail
# Register your models here.
@admin.register(Employee)
class Admin(admin.ModelAdmin):
    list_display = ['id','employeename','phone','email']

@admin.register(Registration)
class registration(admin.ModelAdmin):
    list_display = ['id']

@admin.register(Fail)
class fail(admin.ModelAdmin):
    pass