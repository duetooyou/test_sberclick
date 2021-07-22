from django.contrib import admin
from .models import Category, Claim


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    list_filter = ('status', 'owner', 'category',)
