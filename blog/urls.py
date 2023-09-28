from django.urls import path
from .views import BlogPostListCreateView

urlpatterns = [
    path('all/', BlogPostListCreateView.as_view(), name='blogpost-list-create'),
]
