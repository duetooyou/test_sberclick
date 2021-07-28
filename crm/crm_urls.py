from django.urls import path
from .views import (AllClaimsView,
                    ClaimByCategoryFilter,
                    ClaimByDateFilter,
                    ClaimByDateRangeFilter,
                    ClaimUpdateView,
                    ClaimCreateView,
                    ClaimDeleteView,
                    AllClientsView,
                    ClientDeleteView,
                    ClientCreateView,
                    ClientUpdateView)

urlpatterns = [
    path('claims/', AllClaimsView.as_view(), name='claims_list'),
    path('claims/create/', ClaimCreateView.as_view(), name='claims_create'),
    path('claims/<int:pk>/update/', ClaimUpdateView.as_view(), name='claims_update'),
    path('claims/<int:pk>/delete/', ClaimDeleteView.as_view(), name='claims_delete'),
    path('claims/filter/', ClaimByCategoryFilter.as_view(), name='status_category_filter'),
    path('claims/datefilter/', ClaimByDateFilter.as_view(), name='date_filter'),
    path('claims/daterangefilter/', ClaimByDateRangeFilter.as_view(), name='daterange_filter'),
    path('clients/', AllClientsView.as_view(), name='clients_list'),
    path('clients/<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),
    path('clients/create/', ClientCreateView.as_view(), name='client_create'),
    path('clients/<int:pk>/update/', ClientUpdateView.as_view(), name='client_update'),
]
