from django.urls import path
from . import views
urlpatterns = [
    path("",views.home,name='home-page'),
    path("/hospital",views.hospital,name='hospital-page'),
]
