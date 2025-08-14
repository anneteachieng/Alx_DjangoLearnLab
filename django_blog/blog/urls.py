from django.urls import path
from . import views
from .views import (
    PostListView, PostDetailView,
    PostCreateView, PostUpdateView, PostDeleteView,
    CommentCreateView, CommentUpdateView, CommentDeleteView,
    search_posts, PostByTagListView,
    home, register, profile
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Home & Auth
    path('', PostListView.as_view(), name='home'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),

    # Post CRUD
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # Comments (Class-based views for CRUD)
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),

    # Comments (Function-based views)
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('comments/<int:pk>/edit/', views.comment_edit, name='comment_edit'),
    path('comments/<int:pk>/delete/', views.comment_delete, name='comment_delete'),

    # Search
    path('search/', search_posts, name='search-posts'),

    # Posts filtered by tag
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='post-by-tag'),
]


