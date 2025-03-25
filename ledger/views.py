from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Recipe, RecipeImage
from .forms import RecipeForm, RecipeImageForm


class RecipeListView(ListView):
    model = Recipe
    template_name = 'ledger/recipe_list.html'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'ledger/recipe.html'
    redirect_field_name = 'accounts/login'
    

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = 'ledger/recipe_add.html'
    redirect_field_name = 'accounts/login'
    form_class = RecipeForm


class RecipeImageCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = 'ledger/recipeimage_add.html'
    redirect_field_name = 'accounts/login'
    form_class = RecipeImageForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        return context

    def form_valid(self, form):
        form.instance.recipe = Recipe.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'ledger:recipe',
            kwargs={'pk': self.object.recipe.pk}
            )
