from django.contrib.auth.models import User
from rest_framework import serializers
from ..models import *


class UserSerializer(serializers.ModelSerializer):
    """ A serializer class for the User model """

    class Meta:
        model = User
        # Specify the fields that should be made accessible.
        # Mostly it is all fields in that model
        fields = ('id', 'first_name', 'last_name', 'username',
                  'password', 'is_active', 'is_superuser')


class GenreSerializer(serializers.ModelSerializer):
    """ A serializer for the Genre model """

    class Meta:
        model = Genre
        fields = ('id', 'name', 'description')


class MovieSerializer(serializers.ModelSerializer):
    """ A serializer class for the Movie model """

    class Meta:
        model = Movie
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    """ A serializer class for the Comment model """

    class Meta:
        model = Comment
        fields = ('id', 'user', 'movie', 'comment', 'visible', 'created')
