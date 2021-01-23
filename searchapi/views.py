from rest_framework import viewsets, filters
from .serializers import Searchapiserializers
from .models import Books

class SearchapiViewset(viewsets.ModelViewSet):
    queryset = Books.objects.all().order_by('id')
    serializer_class = Searchapiserializers
    search_fields = ['title','author']
    filter_backends = (filters.SearchFilter,)
