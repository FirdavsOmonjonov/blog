from rest_framework import serializers
from .models import Blog, Like, Comment


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'content', 'created_at', 'uploaded_by', 'viewers']
        read_only_fields = ['id', 'created_at']

    def create(self, validated_data):
        viewers_data = validated_data.pop('viewers', None)
        blog = Blog.objects.create(**validated_data)
        if viewers_data:
            blog.viewers.set(viewers_data)
        return blog


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'author', 'blog', 'created_at']
        read_only_fields = ['id', 'author', 'created_at']



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author', 'blog', 'content']
        read_only_fields = ['id', 'author']

