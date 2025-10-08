from django.urls import path 
from . import views 

urlpatterns = [
    path('mamad', views.mamad),
    path('milad', views.milad),
    path('mehdi', views.mehdi),
    path('amin', views.amin),
]
