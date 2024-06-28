from rest_framework import pagination


class AdPagination(pagination.PageNumberPagination):
    page_size = 10