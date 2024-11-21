"""
URL configuration for main_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from dog_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',login_page, name="login_page"),
    path('logout/',logout_page,name="logout_page"),
    path('signup/',signup_page,name="signup_page"),
    path('search/',search_page,name="search_page"),
    path('list/',list_page,name="list_page"),
    path('view-list/<id>/',view_list,name="view_list")
]
