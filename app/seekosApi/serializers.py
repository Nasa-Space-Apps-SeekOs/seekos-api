from rest_framework import serializers
from rest_framework.authtoken.models import Token
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
        retorno = obj.keys.all()
        return KeysSerializer(retorno, many=True).data
    
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class RepositorySerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()
    keys = serializers.SerializerMethodField()
    members = UserSerializer(many=True, required=False)

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
            'keys',
        ]
    
    def get_likes(self, obj):
        return obj.likes.count()
    
    def get_keys(self, obj):
        retorno = obj.keys.all()
        return KeysSerializer(retorno, many=True).data
    
    def to_internal_value(self, data):
        return super().to_internal_value(data)

    def create(self, validated_data):
        request = self.context.get('request')
        rep = super().create(validated_data)
        # RUserRepositoryMember.objects.create(user=request.user, repository=rep, is_owner=True)
        RUserRepositoryMember.objects.create(user=User.objects.get(id=1), repository=rep, is_property=True)
        return rep


class RepositoryCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepositoryComment
        fields = '__all__'

    created_at = serializers.DateTimeField(format="%d/%m/%Y", read_only=True)
    updated_at = serializers.DateTimeField(format="%d/%m/%Y", read_only=True)

class KeysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keys
        fields = ['name']


class RUserRepositoryMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = RUserRepositoryMember
        fields = '__all__'
