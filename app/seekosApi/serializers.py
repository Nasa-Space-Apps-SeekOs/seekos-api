from rest_framework import serializers
from seekosApi.models import RepositoryComment, Country, User, Repository


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class RepositorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Repository
        fields = '__all__'


class RepositoryCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepositoryComment
        fields = '__all__'
