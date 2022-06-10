"""TestApplication URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt

from TestApplication import settings
from user import views

from rest_framework.authtoken import views as au

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.showIndex,name="main"),
    path('user_signup', views.user_signup,name="user_signup"),
    path('user_login', views.user_login,name="user_login"),
    path('user_registration', views.user_registration,name="user_registration"),
    path('user_login_check', views.user_login_check,name="user_login_check"),
    path('user_profile', views.user_profile,name="user_profile"),
    path('update_profile',views.update_profile,name="update_profile"),
    path('update_data',views.update_data,name="update_data"),
    path('aboutus', views.aboutus, name="aboutus"),
    path('contactus', views.contactus, name="contactus"),
    path('checkmobile/',views.checkmobile,name="checkmobile"),
    path('checkemail/',views.checkemail,name="checkemail"),

    path('generate_token/',au.obtain_auth_token),
    path('api',csrf_exempt(views.InsertSms.as_view())),


]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)