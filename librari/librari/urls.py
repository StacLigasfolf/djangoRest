from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views import AuthorModelViewSet

router = DefaultRouter()
router.register('authors', AuthorModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-token-auth/', obtain_auth-token),
    path(r'^myapi/(?P<version\d>)/authors/$', MyAPIView.as_view()),
]
