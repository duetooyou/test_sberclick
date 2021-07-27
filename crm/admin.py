from django.contrib import admin
from .models import Category, Claim, Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'notification',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    ordering = ('id',)


@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'category',
                    'owner',
                    'status',
                    'created',)
    list_filter = ('id',
                   'status',
                   'category',)
    prepopulated_fields = {'slug': ['name']}
