from .models import Keyword, Category, Document, Context, Review, User

from rest_auth.models import TokenModel
from rest_framework import serializers


class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = ('id', 'name', 'definition')

    def create(self, validated_data):
        instance, _ = Keyword.objects.get_or_create(**validated_data)
        return instance


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description')


class ContextSerializer(serializers.ModelSerializer):
    keyword_given = KeywordSerializer()
    user_reviews = serializers.SerializerMethodField('get_reviews')
    
    def get_reviews(self, obj):
        results = Review.objects.filter(user=self.context['request'].user, context=obj)
        return ReviewSerializer(results, many=True).data

    class Meta:
        model = Context
        fields = ('id', 'position_from', 'position_to', 'text', 'document', 'keyword_given', 'next_context_id', 'prev_context_id', 'user_reviews')
        depth = 1


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('__all__')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('__all__')


class UserSerializer(serializers.ModelSerializer):
    last_context_id = serializers.SerializerMethodField('return_last_context_id')

    def return_last_context_id(self, user):
        try:
            return Review.objects.filter(user=user.id).latest('created').context.id
        except:
            return Context.objects.first().id if Context.objects.first() else None

    class Meta:
        model = User
        fields = ('id', 'username', 'is_staff', 'last_context_id')



class TokenSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = TokenModel
        fields = ('key','user',)
        depth = 1
