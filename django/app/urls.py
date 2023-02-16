from django.urls import path
from .views import Home,Detail
from . import views

urlpatterns = [
    path('',Home.as_view(),name="home"),
    path('<int:pk>/',Detail.as_view(),name="detail"),
    path('order/',views.add,name="add")
    
]
