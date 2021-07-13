from django.contrib import admin
from django.urls import path, include
from attendance import urls

admin.site.site_header = "Attendance Management By NFG"
admin.site.index_title = "Welcome to Dr.Finder NFG"

urlpatterns = [
    path('siteAdminApproveByNFG/', admin.site.urls),
    path('', include('attendance.urls')),
]
