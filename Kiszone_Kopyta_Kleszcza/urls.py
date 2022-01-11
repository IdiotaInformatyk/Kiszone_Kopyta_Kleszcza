from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.contrib import admin
from home import views

urlpatterns = [
    path("registration/", views.registration, name="registration"),
    path('login/', auth_views.LoginView.as_view(template_name='home/login.html'), name='login'),
    path('', include("django.contrib.auth.urls")),

    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('my-profile/', views.my_profile, name='my_profile'),
    path("", views.home, name="home"),
    path('admin/', admin.site.urls),



]
