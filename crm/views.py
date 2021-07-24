from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from django.shortcuts import render
from django.db.models import Q
from .forms import ClaimCreateForm
from .models import Claim, Category


def home_page(request):
    return render(request, template_name='home.html')


class CategoryStatusMixin:
    def get_categories(self):
        return Category.objects.all()

    def get_status(self):
        return [i[0] for i in Claim.STATUS]


class AllClaimsView(LoginRequiredMixin, ListView, CategoryStatusMixin):
    queryset = Claim.objects.all()
    paginate_by = '10'
    context_object_name = 'claims'
    template_name = 'crm/claims/list.html'


class ClaimByCategoryFilter(AllClaimsView, CategoryStatusMixin):
    def get_queryset(self):
        self.request.GET.getlist('status')
        return Claim.objects.filter(Q(category__name__in=self.request.GET.getlist('category')) |
                                    Q(status__in=self.request.GET.getlist('status')))


class AllCategoryView(ListView):
    queryset = Category.objects.all()
    context_object_name = 'categories'
    template_name = 'crm/claims/list.html'


class ClaimCreateView(CreateView):
    queryset = Claim.objects.all()
    form_class = ClaimCreateForm()
    template_name = 'crm/claims/list.html'
