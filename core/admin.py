from django.contrib import admin
from core.models.Employee import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'department')
    list_filter = ('department',)
    fields = ('name', 'email', 'department')
    search_fields = ('name', 'email', 'department')
    ordering = ('name',)
    
admin.site.site_header = "Employees Management"
admin.site.site_url = None
admin.site.index_title = "Luiza Labs"
admin.site.site_title = "Employees"
admin.site.login_template = "admin/login_template_changed.html"
admin.site.register(Employee, EmployeeAdmin)