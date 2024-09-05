from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from ..models import Genre, Movie, Comment
from .serializers import UserSerializer, GenreSerializer, MovieSerializer, CommentSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '',
    ]
    return Response(request, routes)


class Home(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class UserList(generics.ListAPIView):
    """View to list all users"""
    queryset = User.objects.all().order_by('first_name')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserCreate(generics.CreateAPIView):
    """View to create a new user"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """ Retrieve a user or update user information.
        Accepts GET and PUT requests and the record id must be provided in the request """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class GenreListCreate(generics.ListCreateAPIView):
    """View to create a new genre"""
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAuthenticated]


class GenreRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """ Retrieve and update Genre information """
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (permissions.IsAuthenticated,)


class MovieListCreate(generics.ListCreateAPIView):
    """List and create movies """
    queryset = Movie.objects.all().order_by('name')
    serializer_class = MovieSerializer
    permission_classes = (permissions.IsAuthenticated,)


class MovieRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """Retrieve and update a movie"""
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (permissions.IsAuthenticated,)


class CommentListCreate(generics.ListCreateAPIView):
    """ List or create a movie """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticated,)


class CommentRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """ List or create a movie """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticated,)
