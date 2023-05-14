"""
URL configuration for gcm project.

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
from .views import view_balance
from .views import check_balance, check_balance, create_account, credit, debit

urlpatterns = [
    path('<int:account_id>/balance/', view_balance, name='view_balance'),
    path('create-account/', create_account, name='create_account'),
    path('check-balance/', check_balance, name='check_balance'),
    path('credit/', credit, name='credit'),
    path('debit/', debit, name='debit'),
]
