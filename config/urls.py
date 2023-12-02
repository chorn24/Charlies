"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app.views import hub, bltg, about_us,contacts,location_hour,menu,giga


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",hub, name="HUB"),
    path("gigachad/",giga, name="GIGA"),
    path("bryce_loves_this_guy/", bltg, name="chop"),
    path("about_us/",about_us,name="ABOUT"),
    path("contact/",contacts,name="CONTACTS"),
    path("locations_and_hours/",location_hour,name="LOCATION"),
    path("menu/",menu,name="MENU")
]
