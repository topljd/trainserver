from django.contrib import admin
from .models import Department, Excelfile
# Register your models here.

from import_export.admin import ImportExportModelAdmin, ImportExportMixin
from import_export import resources

from mptt.admin import MPTTModelAdmin


class DepartmentResource(resources.ModelResource):

    class Meta:
        model = Department
        fields = ('id', 'name', 'parent',)
        readonly_fields = ('slug',)


@admin.register(Department)
class OrgsAdmin(MPTTModelAdmin):
    mptt_level_indent = 40
    resource_class = DepartmentResource
    list_display = ('name', 'slug',  'parent', 'id')
    readonly_fields = ('slug', 'id',)


@admin.register(Excelfile)
class ExcelfilefileAdmin(admin.ModelAdmin):
    list_display = ('id', 'excelfile')
