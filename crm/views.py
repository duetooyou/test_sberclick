from datetime import date
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from django.shortcuts import render
from django.db.models import Q
from .forms import ClaimCreateForm
from .models import Claim, Category


def home_page(request):
    return render(request, template_name='home.html')


class CategoryStatusDateMixin:
    def get_categories(self):
        return Category.objects.all()

    def get_status(self):
        return [i[0] for i in Claim.STATUS]

    def get_start_date(self):
        start_date = date.today()
        return start_date

    def get_end_date(self):
        end_date = date.today()
        return end_date

    def get_selected_date(self):
        selected_date = date.today()
        return selected_date


class AllClaimsView(LoginRequiredMixin, ListView, CategoryStatusDateMixin):
    queryset = Claim.objects.all()
    paginate_by = '10'
    context_object_name = 'claims'
    template_name = 'crm/claims/list.html'


class ClaimByCategoryFilter(AllClaimsView, CategoryStatusDateMixin):
    def get_queryset(self):
        return Claim.objects.filter(Q(category__name__in=self.request.GET.getlist('category')) |
                                    Q(status__in=self.request.GET.getlist('status')))


class ClaimByDateFilter(AllClaimsView, CategoryStatusDateMixin):
    def get_queryset(self):
        print(self.request.GET.get('selected_date'))
        if self.request.GET.get('selected_date'):
            return Claim.objects.filter(created=self.request.GET.get('selected_date'))
        else:
            return Claim.objects.all()


class ClaimByDateRangeFilter(AllClaimsView, CategoryStatusDateMixin):
    def get_queryset(self):
        if self.request.GET.get('start_date') and self.request.GET.get('end_date'):
            return Claim.objects.filter(created__range=[self.request.GET.get('start_date'),
                                                        self.request.GET.get('end_date')])
        else:
            return Claim.objects.all()


class ClaimCreateView(CreateView):
    queryset = Claim.objects.all()
    form_class = ClaimCreateForm()
    template_name = 'crm/claims/list.html'
