from .views import GenericPostListCreateView, RetrieveDeleteUpdatePostView
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', GenericPostListCreateView.as_view(),name='api'),
    path('token/', obtain_auth_token, name='token'),
    path('<int:pk>/', RetrieveDeleteUpdatePostView.as_view(),name='retrieve')
]