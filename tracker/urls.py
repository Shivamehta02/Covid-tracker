from django.urls import path
from . import views
from django.conf.urls.static import static 
from django.conf import settings
urlpatterns = [
    path("",views.home,name='home-page'),
    path("hospital",views.hospital,name='hospital-page'),
] +  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
