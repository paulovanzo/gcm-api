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
from . import views

app_name = 'accounts'

urlpatterns = [
    path('<int:account_id>/balance/', views.view_balance, name='view_balance'),
    path('create-account/', views.create_account, name='create_account'),
    path('check-account/', views.check_account, name='check_account'),
    path('check-balance/', views.check_balance, name='check_balance'),
    path('credit/', views.credit, name='credit'),
    path('debit/', views.debit, name='debit'),
    path('transfer/', views.transfer, name='transfer'),
    path('yield-interest/', views.yield_interest, name='yield_interest'),
    path('accounts/', views.AccountList.as_view(), name='account-list'),
    path('accounts/<int:pk>/', views.AccountDetail.as_view(), name='account-detail'),
    path('accounts/<int:pk>/credit/', views.CreditView.as_view(), name='account-credit'),
    path('accounts/<int:pk>/debit/', views.DebitView.as_view(), name='account-debit'),
    path('accounts/<int:pk>/transfer/', views.TransferView.as_view(), name='account-transfer'),
    path('accounts/<int:pk>/yield_interest/', views.YieldInterestView.as_view(), name='account-yield-interest'),

]
