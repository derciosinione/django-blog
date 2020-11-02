from django.urls import path
from .views import ( PostCreateView, 
                    PostUpdateView, 
                    PostDeleteView, 
                    PostDetailView, 
                    PostListView, 
                    UserPostListView, about ) 

app_name = 'blog'
urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('about/', about, name='about'),
]
