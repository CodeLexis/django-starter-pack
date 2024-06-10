from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class Pagination(PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'data': data,
            'meta': {
                'pagination_links': {
                    'next': self.get_next_link(),
                    'previous': self.get_previous_link()
                },
                'count': self.page.paginator.count,
            },
        })
