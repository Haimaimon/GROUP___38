import django_filters
from django_filters import CharFilter , ChoiceFilter
from .models import *


class AllJobFilter(django_filters.FilterSet):
    title = CharFilter(field_name = 'title', lookup_expr = 'icontains')
    class Meta:
        model = AllJob
        fields = '__all__'
        exclude = ['hr' , 'desc']