from rest_framework.pagination import PageNumberPagination

class BookPagination(PageNumberPagination):
    page_size = 1
    page_query_param = "p"
    page_size_query_param = "records"
    max_page_size = 40
    last_page_strings = "last"