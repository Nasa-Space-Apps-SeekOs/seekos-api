from django.urls import include, path
from rest_framework import routers
from seekosApi.views import UserViewSet, CountryViewSet, RepositoryViewSet, RepositoryCommentViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet , basename='user')
router.register(r'countries', CountryViewSet, basename='country')
router.register(r'repositories', RepositoryViewSet, basename='repository')
router.register(r'repository-comments', RepositoryCommentViewSet, basename='repository-comment')


urlpatterns = [
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]