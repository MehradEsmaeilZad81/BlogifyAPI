from django.urls import path
from .views import BlogPostListCreateView, BlogPostDetailView

urlpatterns = [
    path('all/', BlogPostListCreateView.as_view(), name='blogpost-list-create'),
    path('all/<int:pk>/', BlogPostDetailView.as_view(), name='blogpost-detail'),
]
