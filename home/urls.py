from django.urls import path
from .views import *

app_nam = "home"
urlpatterns = [
    path('', HomeView.as_view(), name='home'),  # home bhnaeko uta views.py ma banako function 
]


