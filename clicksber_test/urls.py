from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from crm.views import home_page


urlpatterns = [
    path('', home_page),
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(), {'next_page': '/crm/'}, name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('crm/', include('crm.crm_urls'), name='crms')
]
