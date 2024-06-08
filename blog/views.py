from urllib.request import Request
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly
from .serializers import BlogSerializer, LikeSerializer, CommentSerializer
from rest_framework import viewsets
from .models import Blog, Like, Comment

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user.username)


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        author = self.request.user
        blog = serializer.validated_data.get('blog')

        existing_like = Like.objects.filter(author=author, blog=blog).first()
        if existing_like:
            existing_like.delete()
        else:
            serializer.save(author=author)



class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
