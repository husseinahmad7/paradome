from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'HusseinAh'
urlpatterns = [
    path('', views.home, name='home'),
    path('glass', views.glass, name= 'glass'),
    path('ex', views.example, name='ex')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)