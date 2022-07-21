from django.urls import path
from . import views


app_name = 'posts'
urlpatterns = [
    path('', views.PostsList.as_view(), name='index'),
    path('<int:pk>/', views.PostView.as_view(), name='post-detail'),
    path('new/', views.PostCreateView.as_view(), name='post-create'),
    path('<int:pk>/update', views.PostUpdateView.as_view(), name='post-update'),
    path('<int:pk>/delete', views.PostDeleteView.as_view(), name='post-delete'),
    path('user/<str:username>/', views.UserPostsList.as_view(), name='user-posts'),
    path('stream/', views.StreamView.as_view(), name='stream'), 
    path('tag/<str:tag>/', views.tag_view, name='tags'),
    path('<int:pk>/like/', views.like, name='like'),
    path('<int:pk>/fav/', views.favorites, name='favorite'),
    path('follow/<str:username>/<option>/', views.follow, name='follow'),
    path('addtag/', views.addTag.as_view(), name='addtag'),
    path('<int:pk>/new', views.DomePostCreateView.as_view(), name='domepost-create'),
    path('dposts/<int:pk>/', views.HtmxDomePostsView.as_view(),name='htmxdomeposts')
    
    
    # # ex: /testdemo/5/results/
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # # ex: /testdemo/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]