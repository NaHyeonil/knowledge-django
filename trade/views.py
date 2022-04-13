from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from trade.serializers import TradeSerializer, TradeCreateSerializer
from trade.models import Trade


class TradePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1


class TradeViewSet(viewsets.ModelViewSet):
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer
    pagination_class = TradePagination

    def get_queryset(self):
        qs = super().get_queryset()

        query = self.request.query_params.get("query", "")
        if query:
            qs = qs.filter(title__icontains=query)

        return qs

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return TradeCreateSerializer
        else:
            return TradeSerializer
