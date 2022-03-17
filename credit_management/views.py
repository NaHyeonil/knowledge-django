from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from credit_management.models import CreditManagement
from credit_management.serializers import CreditManagementSerializer, CreditManagementCreateSerializer


class CreditManagementPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1


class CreditManagementViewSet(viewsets.ModelViewSet):
    queryset = CreditManagement.objects.all()
    serializer_class = CreditManagementSerializer
    pagination_class = CreditManagementPagination

    def get_queryset(self):
        qs = super().get_queryset()

        query = self.request.query_params.get("query", "")
        if query:
            qs = qs.filter(title__icontains=query)

        return qs

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return CreditManagementCreateSerializer
        else:
            return CreditManagementSerializer
