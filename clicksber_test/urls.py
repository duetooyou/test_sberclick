from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from crm.views import home_page


urlpatterns = [
    path('bday_vlada', home_page, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('crm/', include('crm.crm_urls'), name='crms'),
]
