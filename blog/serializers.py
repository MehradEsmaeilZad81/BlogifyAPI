from rest_framework import serializers
from .models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ('id', 'title', 'content', 'author', 'publication_date')


class BlogEditSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200, required=False)
    content = serializers.CharField(required=False)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
