from django.urls import path
from . import views
from django.conf.urls.static import static 
from django.conf import settings

urlpatterns = [
    path('start/', views.index, name="index"),
    path('', views.index, name="index")    
]  
#Allow images to be
urlpatterns += static(settings.MEDIA_URLS, document_root=settings.MEDIA_ROOT)