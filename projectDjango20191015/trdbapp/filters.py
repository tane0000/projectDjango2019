from django_filters import filters
from django_filters import FilterSet

from .models import Trouble

class MyOrderingFilter(filters.OrderingFilter):
    descending_fmt = '%s （降順）'

class TroubleFilter(FilterSet):
    trouble_name = filters.CharFilter(label='不具合件名 ※部分一致', lookup_expr='contains')
    trouble_location = filters.CharFilter(label='発生部位 ※部分一致', lookup_expr='contains')
    occurrence_datetime = filters.DateFilter(label='開始日', lookup_expr='gte')
    input_date = filters.DateFilter(label='入力日', lookup_expr='gte')

#    first_date = filters.DateTimeFilter(label='開始日付時', lookup_expr='lte')
#    last_date = filters.DateTimeFilter(label='終了日付', lookup_expr='gte')
#    score_range = filters.RangeFilter(name='score')
#    date_range = filters.RangeFilter(created_at__range=(first_date,last_date))

#    trouble_machine = filters.CharFilter(name='trouble_machine', label='不具合機器', lookup_expr='contains')

#    user_name = filters.ChoiceFilter(choices=models.Bruser.name, name='user_name', label='物件名', lookup_expr='contains')
#    user_name = filters.ChoiceFilter(choices=models.Bruser.name, label='物件名')
#    trouble_machine = filters.ChoiceFilter(choices=models.Brmachine.name, label='不具合機器')

#    trouble_name = filters.CharFilter(name='trouble_name', label='不具合件名', lookup_expr='contains')
#    occurrence_datetime = filters.DateTimeFilter(name='occurrence_datetime', label='発生日時', lookup_expr='gte')

    class Meta:
        model = Trouble
        fields = (
            'user_name',
            'trouble_name',
            'trouble_machine',
            'trouble_location',
            'disposal_category',
            'occurrence_datetime',
            'input_date',
        )
