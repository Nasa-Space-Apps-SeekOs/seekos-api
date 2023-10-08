import django_filters
from seekosApi.models import Repository
from django.conf import settings
from django.db.models import Q
import requests

class RepositoryFilter(django_filters.FilterSet):
    class Meta:
        model = Repository
        fields = ['search', 'key']

    search = django_filters.CharFilter(method='filter_by_search', label='Search')
    key = django_filters.CharFilter(field_name='keys__name', distinct=True)
    type = django_filters.CharFilter(field_name='type',)
    status = django_filters.CharFilter(field_name='status')

    def filter_by_search(self, queryset, name, value):
        """
        retorno da API: {'keywords': ['foquete_na_rua'], 'tags': []}
        """
        params = {'value': value}
        response = requests.get(settings.SEARCH_API, params=params)

        if response.status_code == 200:
            data = response.json()
            search = '%'.join(data['keywords'])
            queryset = queryset.filter(
                Q(name__icontains=search) |
                Q(resume__icontains=search) |
                Q(body__icontains=search) |
                Q(type__icontains=search)
            )
            return queryset.filter(keys__name__in=data['tags'])
        else:
            return queryset.filter(
                Q(name__icontains=value) |
                Q(resume__icontains=value) |
                Q(body__icontains=value) |
                Q(type__icontains=value)
            )
