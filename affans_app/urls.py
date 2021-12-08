from . import views
from django.urls import path

# supporting just one view localhost:8000/
urlpatterns = [
    path('',views.main_view)
]