from django.shortcuts import render
from rest_framework import viewsets
from seekosApi.models import User, Country, Repository, RepositoryComment, Keys, RUserRepositoryMember
from seekosApi.serializers import UserSerializer, CountrySerializer, RepositorySerializer, RepositoryCommentSerializer, KeysSerializer, RUserRepositoryMemberSerializer
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from seekosApi.filters import RepositoryFilter
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer   


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class RepositoryViewSet(viewsets.ModelViewSet):
    queryset = Repository.objects.all()
    serializer_class = RepositorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = RepositoryFilter

    @action(detail=True, methods=['get'])
    def comments(self, request, pk=None):
        repository = self.get_object()
        comments = repository.repositorycomment_set.all()
        serializer = RepositoryCommentSerializer(comments, many=True)
        return Response(serializer.data)


class RepositoryCommentViewSet(viewsets.ModelViewSet):
    queryset = RepositoryComment.objects.all()
    serializer_class = RepositoryCommentSerializer


class KeysViewSet(viewsets.ModelViewSet):
    queryset = Keys.objects.all()
    serializer_class = KeysSerializer


class RUserRepositoryMemberViewSet(viewsets.ModelViewSet):
    queryset = RUserRepositoryMember.objects.all()
    serializer_class = RUserRepositoryMemberSerializer