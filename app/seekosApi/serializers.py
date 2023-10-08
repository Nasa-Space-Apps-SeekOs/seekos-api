from rest_framework import serializers
from seekosApi.models import RepositoryComment, Country, User, Repository, Keys, RUserRepositoryMember


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    keys = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id',
            'full_name',
            'username',
            'keys'
        ]

    def get_full_name(self, obj):
        return obj.get_full_name()
    
    def get_keys(self, obj):
        return obj.keys.all()


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class RepositorySerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()
    members = UserSerializer(many=True)

    class Meta:
        model = Repository
        fields = [
            'id',
            'name',
            'resume',
            'body',
            'url_image',
            'url_project',
            'type',
            'status',
            'ranking',
            'created_at',
            'updated_at',
            'members',
            'likes',
        ]
    
    def get_likes(self, obj):
        return obj.likes.count()


class RepositoryCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepositoryComment
        fields = '__all__'


class KeysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keys
        fields = '__all__'


class RUserRepositoryMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = RUserRepositoryMember
        fields = '__all__'
