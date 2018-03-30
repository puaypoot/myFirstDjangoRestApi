from rest_framework import viewsets
from .serializers import AttributeSerializer
from .models import Attribute
from rest_framework.response import Response
from django.core import serializers
import json

class AttributeView(viewsets.ModelViewSet):

    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer

    def set_data_format(self, data):
        new_data = []
        for row in data:
            new_data.append({
                'id': row['pk'],
                'name': row['fields']['name'],
                'date_created': row['fields']['date_created'],
                'date_modified': row['fields']['date_modified']
            })
        return new_data

    def list(self, request):
        data = Attribute.objects.filter(name=request.GET['name']) if len(request.GET) > 0 else Attribute.objects.filter()
        data = json.loads(serializers.serialize("json", data))
        return Response(data={
            'query_params': request.GET,
            'data': self.set_data_format(data) if len(data)>0 else []
            }, status=200)

    # def create(self, request):
    #     print('create')
    #     pass

    # def retrieve(self, request, pk=None):
    #     print('retrieve')
    #     pass

    # def update(self, request, pk=None):
    #     print('update')
    #     pass

    # def partial_update(self, request, pk=None):
    #     print('partial_update')
    #     pass

    # def destroy(self, request, pk=None):
    #     return Response(data={
    #         'query_params': {
    #             'pk': pk
    #         },
    #         # 'data': self.set_data_format(data) if len(data)>0 else []
    #         }, status=200)