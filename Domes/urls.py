from django.urls import path
from . import views


app_name = 'domes'
urlpatterns = [
    path('', views.ExploreDomesView.as_view(),name='explore'),
    path('new/', views.DomeCreateView.as_view(),name='dome-create'),
    path('<int:pk>/',views.DomeView.as_view(),name='dome-detail'),
    path('<int:pk>/newcategory/',views.CategoryCreateView.as_view(),name='category-create'),
]