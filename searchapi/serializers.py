from rest_framework import serializers
from .models import Books

class Searchapiserializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Books
        fields = ['id','title','description','author']