from rest_framework.filters import BaseFilterBackend
import coreapi


class NameFilterBackend(BaseFilterBackend):
    def get_schema_fields(self, view):
        fields = [
            coreapi.Field(
                name='name',
                location='query',
                required=False,
                type='string',
                description='Filter by name',
                ),
            coreapi.Field(
                name='region',
                location='query',
                required=False,
                type='int',
                description='Filter by region',
                ),
            coreapi.Field(
                name='district',
                location='query',
                required=False,
                type='int',
                description='Filter by district',
                )
            ]
        return fields

    def filter_queryset(self, request, queryset, view):
        try:
            if 'name' in request.query_params:
                c_name = request.query_params['name']
                queryset = queryset.filter(company_name__icontains=c_name)
            if 'region' in request.query_params:
                c_region = request.query_params['region']
                queryset = queryset.filter(company_region=c_region)
            if 'district' in request.query_params:
                c_district = request.query_params['district']
                queryset = queryset.filter(company_district=c_district)
        except KeyError:
            # no query parameters
            pass
        return queryset
