from rest_framework import pagination

class SmileAPIPagination(pagination.PageNumberPagination):
    page_size = 5