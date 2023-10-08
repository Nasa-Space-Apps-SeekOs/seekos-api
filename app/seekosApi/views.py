from rest_framework import viewsets
from seekosApi.models import User, Country, Repository, RepositoryComment, Keys, RUserRepositoryMember
from seekosApi.serializers import UserSerializer, CountrySerializer, RepositorySerializer, RepositoryCommentSerializer, KeysSerializer, RUserRepositoryMemberSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from seekosApi.filters import RepositoryFilter


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
    
    @action(detail=True, methods=['post'], url_path='comments')
    def post_comment(self, request, pk=None):
        repository = self.get_object()
        comment = RepositoryComment.objects.create(
            repository=repository,
            user=request.user,
            comment=request.data.get('comment')
        )
        comment.save()
        serializer = RepositoryCommentSerializer(comment)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def members(self, request, pk=None):
        repository = self.get_object()
        members = repository.ruserrepositorymember_set.all()
        serializer = RUserRepositoryMemberSerializer(members, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'], url_path='members')
    def post_member(self, request, pk=None):
        repository = self.get_object()
        member = RUserRepositoryMember.objects.create(
            repository=repository,
            user=User.objects.get(id=1)
        )
        member.save()
        serializer = RUserRepositoryMemberSerializer(member)
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