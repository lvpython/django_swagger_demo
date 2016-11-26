from django.conf.urls import include, patterns, url

from rest_framework import routers
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer

from views.dictionary_view import DictionaryViewSet

schema_view = get_schema_view(
    title='Example API',
    renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer]
)

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'hanzi', DictionaryViewSet)

urlpatterns = patterns(
  '',
  url(r'^', include(router.urls)),
  url(r'^swagger/$', schema_view),
 )