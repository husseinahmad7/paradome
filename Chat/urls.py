from django.urls import path
from . import views


app_name = 'chat'
urlpatterns = [
    path('<int:pk>/', views.ChatMessageList.as_view(), name='chat-channel'),
    path('<int:pk>/new', views.ChatChannelCreateView.as_view(), name='chatchannel-create')
]