from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework import serializers

from .models import Author, Book, Biography, Article


class AuthorModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        
class BiographySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Biography
        fields = '__all__'

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article