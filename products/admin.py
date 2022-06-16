from django.contrib import admin
from .models import Products,Comment
# Register your models here.
class InlineComment(admin.TabularInline):
    model = Comment
    extra = 0

class ProductAdmin(admin.ModelAdmin):
    inlines = [InlineComment]






admin.site.register(Products,ProductAdmin)
admin.site.register(Comment)