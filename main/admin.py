from django.contrib import admin

from .models import Category, Recipe, Image

class ImageInlineAdmin(admin.TabularInline):
    model = Image
    Fields = ('image', )
    max_num = 5

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [ImageInlineAdmin,]


admin.site.register(Category)
