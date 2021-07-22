from django.urls import path
from .views import AllClaimsView

urlpatterns = [
    path('claims/', AllClaimsView.as_view())
]
