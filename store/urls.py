from django.urls import path
from . import views
app_name = 'store'
urlpatterns = [
    path('', views.StoreView,name='StoreIndex'),
    path('<int:pk>/', views.ProductView, name='Product_detail'),
    path('addtocart/<int:product_id>/', views.Add_to_Cart, name='addtocart')
    ]