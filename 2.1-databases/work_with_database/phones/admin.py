from django.contrib import admin


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    slug = {"slug": ["name"]}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", )}


