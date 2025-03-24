from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient, RecipeImage


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


class RecipeImageInline(admin.TabularInline):
    model = RecipeImage


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInline, RecipeImageInline]


class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    inlines = [RecipeIngredientInline]


class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient


class RecipeImageAdmin(admin.ModelAdmin):
    model = RecipeIngredient


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(RecipeImage, RecipeImageAdmin)
