"""PyPress URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("blog.urls")),
    path('register/', user_views.userRegistration, name="user_registration"),
    path('login/', auth_views.LoginView.as_view(template_name="users/login.html"), name="user_login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"), name="user_logout"),
    path('pw-reset/', auth_views.PasswordResetView.as_view(template_name="users/password_reset.html"), name="password_reset"),
    path('pw-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"), name="password_reset_done"),
    path('pw-reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"), name="password_reset_confirm"),
    path('pw-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"), name="password_reset_complete"),
    path('profile/', user_views.userProfile, name="user_profile"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "PyPress Admin"
admin.site.site_title = "PyPress Admin Portal"
admin.site.index_title = "Welcome to PyPress administration panel"