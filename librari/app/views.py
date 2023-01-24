from rest_framework.viewsets import ModelViewSet
from .models import Author
from .serializers import AuthorModelSerializer
from rest_framework import viewsets


class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer


class ArticleCreateAPIView(CreateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleViewSet(viewsets.ViewSet):
    renderer_classes = [JSONRenderer]

    def list(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        article = get_object_or_404(Article, pk=p)
