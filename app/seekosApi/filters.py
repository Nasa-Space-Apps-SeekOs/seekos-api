import django_filters
from seekosApi.models import Repository


class RepositoryFilter(django_filters.FilterSet):
    class Meta:
        model = Repository
        fields = ['search', 'key']

    search = django_filters.CharFilter(method='filter_by_search', label='Search')
    key = django_filters.CharFilter(field_name='keys__name', distinct=True)
    type = django_filters.CharFilter(field_name='type',)
    status = django_filters.CharFilter(field_name='status')

    def filter_by_search(self, queryset, name, value):
        return queryset.filter(
            django_filters.Q(name__icontains=value) |
            django_filters.Q(resume__icontains=value) |
            django_filters.Q(body__icontains=value) |
            django_filters.Q(type__icontains=value)
        )
