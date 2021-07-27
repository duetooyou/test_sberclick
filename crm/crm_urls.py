from django.urls import path
from .views import (AllClaimsView,
                    ClaimByCategoryFilter,
                    ClaimByDateFilter,
                    ClaimByDateRangeFilter,
                    ClaimDetailView,
                    ClaimCreateView,
                    AllClientsView,
                    ClientDeleteView,
                    ClientCreateView,
                    ClientUpdateView)

urlpatterns = [
    path('claims/', AllClaimsView.as_view(), name='claims_list'),
    path('claims/create/', ClaimCreateView.as_view(), name='claims_create'),
    path('claims/filter/', ClaimByCategoryFilter.as_view(), name='status_category_filter'),
    path('claims/datefilter/', ClaimByDateFilter.as_view(), name='date_filter'),
    path('claims/daterangefilter/', ClaimByDateRangeFilter.as_view(), name='daterange_filter'),
    path('clients/', AllClientsView.as_view(), name='clients_list'),
    path('clients/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),
    path('clients/create/', ClientCreateView.as_view(), name='client_create'),
    path('clients/<int:pk>', ClientUpdateView.as_view(), name='client_update'),
    path('claims/<slug:slug>/', ClaimDetailView.as_view(), name='claims_detail'),
]
