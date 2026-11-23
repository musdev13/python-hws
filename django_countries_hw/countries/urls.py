from django.urls import path

from . import views

urlpatterns = [
    path('', views.countries, name='countries'),
    path('country/<str:code>/', views.country_detail, name='country_detail'),
    path('capital/<str:code>/', views.capital_detail, name='capital_detail'),
    path('regions/', views.regions, name='regions'),
    path('region/<str:code>/', views.region_detail, name='region_detail'),
    path('languages/', views.languages, name='languages'),
]
