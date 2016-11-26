# -*- coding: utf-8 -*-

import logging

from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.serializers import HanziSetSerializer
from dictionary.models import HanziSet

class DictionaryViewSet(ModelViewSet):
    logger = logging.getLogger(__name__)
    serializer_class = HanziSetSerializer
    queryset = HanziSet.objects.all()

    @list_route(methods=['post'], url_path='search')
    def hanzi_search(self, request):
        #hanzi_char = request.data['hanzi_char']
        #hanzi_pic_id = request.data['hanzi_pic_id']
        instance = HanziSet.objects.first()
        serializer = HanziSetSerializer(instance)
        #return Response(serializer.data)
        demo_data = {
          'dicts': [
              { 'name': u'unicode', 'value': [u'U+6DE8'] },
              { 'name': u'台湾', 'value': [u'A00001/明', u'A02758-005/盲', u'A02398-001/盟'] },
              { 'name': u'汉语', 'value': [u'hy-8-0001-01'] },
              { 'name': u'高丽', 'value': [u'明2/盲'] },
              { 'name': u'敦煌', 'value': [u'dh-001-01'] }
          ],
          'similar_parts': u'水爪川',
          'mix_split': '',
        }
        return Response(demo_data)


