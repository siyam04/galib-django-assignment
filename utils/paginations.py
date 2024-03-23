from rest_framework.response import Response
from rest_framework.pagination import BasePagination


class OffsetLimitPagination(BasePagination):

    def paginate_queryset(self, queryset, request, view=None):
        offset = int(request.query_params.get('offset', 0))
        limit = int(request.query_params.get('limit', 12))
        self.offset = offset
        self.limit = limit
        return queryset[offset:offset+limit]

    def get_paginated_response(self, data):
        return Response(data)
