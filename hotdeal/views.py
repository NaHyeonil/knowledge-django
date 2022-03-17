from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from hotdeal.models import Hotdeal
from hotdeal.serializers import HotdealSerializer, HotdealCreateSerializer


class HotdealPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1


class HotdealViewSet(viewsets.ModelViewSet):
    queryset = Hotdeal.objects.all()
    serializer_class = HotdealSerializer
    pagination_class = HotdealPagination

    def get_queryset(self):
        qs = super().get_queryset()

        query = self.request.query_params.get("query", "")
        if query:
            qs = qs.filter(title__icontains=query)

        return qs

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return HotdealCreateSerializer
        else:
            return HotdealSerializer
