from django.contrib import admin
from .models import Article, Tag, Scope


class RelationshipInline(admin.TabularInline):
    model = Scope

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    pass
