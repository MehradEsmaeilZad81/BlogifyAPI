from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import BlogPost
from .serializers import BlogPostSerializer, BlogEditSerializer
from django.shortcuts import get_object_or_404


class BlogPostListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        blog_posts = BlogPost.objects.all()
        serializer = BlogPostSerializer(blog_posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        request.data['author'] = request.user.pk
        serializer = BlogPostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        title = serializer.validated_data['title']
        if BlogPost.objects.exclude(pk=request.user.pk).filter(title=title).exists():
            return Response({'message': 'BlogPost with this title already exists'}, status=status.HTTP_400_BAD_REQUEST)
        BlogPost.objects.create(**serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class BlogPostDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        blog_post = get_object_or_404(BlogPost, pk=pk)
        serializer = BlogPostSerializer(blog_post)
        return Response(serializer.data)

    def put(self, request, pk):
        blog_post = get_object_or_404(BlogPost, pk=pk)
        if request.user.pk != blog_post.author.pk:
            return Response({'message': 'You are not the author of this blog post'}, status=status.HTTP_403_FORBIDDEN)
        request.data['author'] = request.user.pk
        serializer = BlogEditSerializer(blog_post, data=request.data)
        serializer.is_valid(raise_exception=True)
        if 'title' in serializer.validated_data:
            updated_title = serializer.validated_data['title']
            if BlogPost.objects.exclude(pk=pk).filter(title=updated_title).exists():
                return Response({'message': 'BlogPost with this title already exists'}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        blog_post = get_object_or_404(BlogPost, pk=pk)
        if request.user.pk != blog_post.author.pk:
            return Response({'message': 'You are not the author of this blog post'}, status=status.HTTP_403_FORBIDDEN)
        blog_post.delete()
        return Response({'message': 'Blog post deleted'}, status=status.HTTP_204_NO_CONTENT)
