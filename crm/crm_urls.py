from django.urls import path
from .views import (AllClaimsView,
                    ClaimByCategoryFilter,
                    ClaimByDateFilter,
                    ClaimByDateRangeFilter,)

urlpatterns = [
    path('claims/', AllClaimsView.as_view(), name='claims_list'),
    path('claims/filter/', ClaimByCategoryFilter.as_view(), name='status_category_filter'),
    path('claims/datefilter/', ClaimByDateFilter.as_view(), name='date_filter'),
    path('claims/daterangefilter/', ClaimByDateRangeFilter.as_view(), name='daterange_filter'),

]
