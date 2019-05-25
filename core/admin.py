from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from core.models.Employee import Employee
from django.core import serializers
from django.http import HttpResponse


def export_as_json(modeladmin, request, queryset):
    response = HttpResponse(content_type="application/json")
    serializers.serialize("json", queryset, stream=response)
    return response

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'department')
    list_filter = ('department',)
    search_fields = ('name', 'email', 'department')
    ordering = ('name',)

    fieldsets = (
        ('Personal data', {
            'fields': ('name', 'email')
        }),
        ('Department', {
            'fields': ('department',)
        }),
    )

    actions = [
        'change_department_to_mobile',
        'change_department_to_architeture',
        'change_department_to_ecommerce',
    ]

    def change_department_to_mobile(self, request, queryset):
        queryset.update(department='M')
        self.message_user(request, "Successfully department changed.")

    def change_department_to_architeture(self, request, queryset):
        queryset.update(department='A')
        self.message_user(request, "Successfully department changed.")


    def change_department_to_ecommerce(self, request, queryset):
        queryset.update(department='E')
        self.message_user(request, "Successfully department changed.")

    change_department_to_mobile.short_description = "Change selected employees department to mobile"
    change_department_to_architeture.short_description = "Change selected employees department to architeture"
    change_department_to_ecommerce.short_description = "Change selected employees department to e-commerce"

admin.site.site_header = "Employees Management"
admin.site.site_url = None
admin.site.index_title = "Luiza Labs"
admin.site.site_title = "Employees"
admin.site.login_template = "admin/login_changed.html"
admin.site.register(Employee, EmployeeAdmin)
admin.site.add_action(export_as_json, 'Export selected json')
