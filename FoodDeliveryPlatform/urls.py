"""FoodDeliveryPlatform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
import Account.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Account.views.getLoginPage),
    path('register',Account.views.getRegisterPage,name="register"),
    path('loginUrl',Account.views.login),
    path('registerUrl',Account.views.register),
    path('checkAccountValid', Account.views.checkAccountValid)
]
