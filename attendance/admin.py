from django.contrib import admin
from .models import Employee , Attedance
from import_export.admin import ImportExportModelAdmin

@admin.register(Employee)
@admin.register(Attedance)
class usrdet(ImportExportModelAdmin):
    pass