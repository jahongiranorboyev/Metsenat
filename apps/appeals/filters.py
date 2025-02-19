from django_filters import FilterSet, filters

from apps.appeals.models import Appeal

class AppealFilter(FilterSet):
     from_amount = filters.NumberFilter(field_name = 'amount',lookup_expr = 'gte')
     to_amount =  filters.NumberFilter(field_name ='amount',lookup_expr = 'lte')
     class Meta:
      model = Appeal
      fields={
	    'created_at':['lte','gte'],
	    'status':['exact'],
	    }
