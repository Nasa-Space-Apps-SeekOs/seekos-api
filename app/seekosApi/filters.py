import django_filters
from seekosApi.models import Repository
from django.conf import settings
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
                django_filters.Q(name__icontains=search) |
                django_filters.Q(resume__icontains=search) |
                django_filters.Q(body__icontains=search) |
                django_filters.Q(type__icontains=search)
            )
            return queryset.filter(keys__name__in=data['tags'])
        else:
            return queryset.filter(
                django_filters.Q(name__icontains=value) |
                django_filters.Q(resume__icontains=value) |
                django_filters.Q(body__icontains=value) |
                django_filters.Q(type__icontains=value)
            )
