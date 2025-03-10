from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Recipe


class RecipeListView(ListView):
    model = Recipe
    template_name = 'ledger/recipe_list.html'


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'ledger/recipe.html'
