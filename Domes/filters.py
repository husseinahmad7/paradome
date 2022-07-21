import django_filters
from .models import Dome
from django.db.models import Q

class DomeFilter(django_filters.FilterSet):
    q = django_filters.CharFilter(method='title_description_search', label='search')
    date = django_filters.DateTimeFromToRangeFilter(field_name='date')
    class Meta:
        model = Dome
        fields = ['q','date']
    def title_description_search(self, queryset, name, value):
        return queryset.filter(Q(title__icontains=value) | Q(description__icontains=value))