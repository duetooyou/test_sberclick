from django.shortcuts import render
from .models import Claim
from django.views.generic import ListView


class AllClaimsView(ListView):
    context_object_name = 'claims'
    template_name = 'crm/claims/list.html'

    def get_queryset(self):
        if self.request.GET.get('message') == 'open':
            return Claim.objects.filter(status='open')
        elif self.request.GET.get('message') == 'in_progress':
            return Claim.objects.filter(status='in_progress')
        elif self.request.GET.get('message') == 'closed':
            return Claim.objects.filter(status='closed')
        else:
            return Claim.objects.all()

