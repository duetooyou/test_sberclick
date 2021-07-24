from django.urls import path
from .views import AllClaimsView, ClaimByCategoryFilter

urlpatterns = [
    path('claims/', AllClaimsView.as_view(), name='claims_list'),
    path('claims/filter/', ClaimByCategoryFilter.as_view(), name='category_filter')
]
