from django.urls import include, path
from rest_framework import routers
from seekosApi.views import UserViewSet, CountryViewSet, RepositoryViewSet, RepositoryCommentViewSet, KeysViewSet, RUserRepositoryMemberViewSet
from rest_framework.authtoken.views import obtain_auth_token 

router = routers.DefaultRouter()
router.register(r'users', UserViewSet , basename='user')
router.register(r'countries', CountryViewSet, basename='country')
router.register(r'repositories', RepositoryViewSet, basename='repository')
router.register(r'repository-comments', RepositoryCommentViewSet, basename='repository-comment')
router.register(r'keys', KeysViewSet, basename='keys')
router.register(r'r-user-repository-members', RUserRepositoryMemberViewSet, basename='r-user-repository-member')


urlpatterns = [
    path('', include(router.urls)),
     path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]