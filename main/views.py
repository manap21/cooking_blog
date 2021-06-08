from django.shortcuts import render, get_object_or_404

from .models import *


def index(request):
    return render(request, 'index.html')

def category_detail(request, slug):
    category = Category.objects.get(slug=slug)
    recipes = Recipe.objects.filter(category_id=slug)
    return render(request, 'category-detail.html', locals())

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    image = recipe.get_image
    images = recipe.images.exclude(image=image)
    return render(request, 'recipe-detail.html', locals())