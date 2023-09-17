from django.urls import path
from . import views

urlpatterns=[
    path('',views.home),
    path('python',views.python)
    
]