from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from point_management.models import PointManagement
from point_management.serializers import PointManagementSerializer, PointManagementCreateSerializer


class PointManagementPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1


class PointManagementViewSet(viewsets.ModelViewSet):
    queryset = PointManagement.objects.all()
    serializer_class = PointManagementSerializer
    pagination_class = PointManagementPagination

    def get_queryset(self):
        qs = super().get_queryset()

        query = self.request.query_params.get("query", "")
        if query:
            qs = qs.filter(title__icontains=query)

        return qs

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return PointManagementCreateSerializer
        else:
            return PointManagementSerializer
