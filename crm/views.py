from django.shortcuts import render
from .models import Claim
from django.views.generic import ListView, CreateView
from .forms import ClaimCreateForm


class AllClaimsView(ListView):
    context_object_name = 'claims'
    template_name = 'crm/claims/list.html'

    def get_queryset(self):
        return Claim.objects.filter()


class ClaimCreateView(CreateView):
    queryset = Claim.objects.all()
    form_class = ClaimCreateForm
    template_name = 'crm/claims/list.html'
