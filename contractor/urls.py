from django.urls import path
from . import views


urlpatterns = [
    path('', views.contractor, name='contractors'),
    path('people/', views.people, name='people'),
]
