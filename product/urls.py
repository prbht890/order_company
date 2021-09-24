from django.urls import path
from .views import *

urlpatterns = [
    path('create',ProductCreate.as_view()),
    path('show',ProductView.as_view()),

   
]