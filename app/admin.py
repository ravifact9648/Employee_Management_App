from django.contrib import admin

# Register your models here.
from django.contrib import admin
from app.models import Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=('name','designation','email')

admin.site.register(Employee,EmployeeAdmin)
# admin.site.register()
