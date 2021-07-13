from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    # Basic Page For Everyone
    url(r'^$', RedirectView.as_view(url='dashboard')),
    path('dashboard', views.index, name="Main Page"),
    path('add_employee', views.add_employee, name="Add Employee"),
    path('detail_employee', views.detail_employee, name="Detail Employee"),
    path('add_attendance', views.add_attendance, name="Add Attendance"),
    path('detail_attendance', views.detail_attendance, name="Detail Attendance"),
    
    path('update_employee/<int:id>', views.update_employee, name="Update Employee"),
    path('delete_employee/<int:id>', views.delete_employee, name="Delete Employee"),
    
    path('delete_attedance/<int:id>', views.delete_attendance, name="Delete Attedance"),
    
    path('login', views.handleLogin, name="Login Page"),
    path('logout', views.handleLogout, name="Logout Page"),

] + static(settings.MEDIA_URL,
           document_root=settings.MEDIA_ROOT)
