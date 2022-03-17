from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from knowledge_share.models import Knowledge_Share
from knowledge_share.serializers import Knowledge_ShareSerializer, Knowledge_ShareCreateSerializer


class Knowledge_SharePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1


class Knowledge_ShareViewSet(viewsets.ModelViewSet):
    queryset = Knowledge_Share.objects.all()
    serializer_class = Knowledge_ShareSerializer
    pagination_class = Knowledge_SharePagination

    def get_queryset(self):
        qs = super().get_queryset()

        query = self.request.query_params.get("query", "")
        if query:
            qs = qs.filter(title__icontains=query)

        return qs

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return Knowledge_ShareCreateSerializer
        else:
            return Knowledge_ShareSerializer
