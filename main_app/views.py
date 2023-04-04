from django.shortcuts import render
from .models import Recipe, Ingredient
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import JsonResponse, HttpResponse
# Create your views here.


def home(request):
    recipe = Recipe.objects.filter()

    appetizers = Recipe.objects.filter(category='Appetizer')
    entree = Recipe.objects.filter(category='Entree')
    dessert = Recipe.objects.filter(category='Dessert')
    beverage = Recipe.objects.filter(category='Beverage')
    side = Recipe.objects.filter(category='Side')
    baked_good = Recipe.objects.filter(category='Baked Good')

    return render(request, 'home.html',
                  {'recipes': recipe, 'appetizers': appetizers, 'dessert': dessert,
                      'entree': entree, 'beverage': beverage, 'side': side, 'bake_good': baked_good}
                  )


class RecipeCreate(CreateView):
    model = Recipe
    fields = ['name', 'category', 'day_of_week', 'img_url']
    success_url = '/recipes'


class RecipeUpdate(UpdateView):
    model = Recipe
    fields = ['name', 'category', 'day_of_week', 'img_url']
   


class RecipeDelete(DeleteView):
    model = Recipe
    success_url = '/recipes'


def recipes_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(request, 'detail.html', {
        'recipe': recipe,
    })


def recipes(request):
    all_recipes = Recipe.objects.filter()

    return render(request, 'recipes.html', {'recipes': all_recipes})


def meal_plan(request):
    return render(request, 'meal_plan.html')

def get_ingredients(request):
    ingredients = Ingredient.objects.filter()
    return JsonResponse({'ingredients':list(ingredients.values())})

def recipe_add_test(request):
    return render(request, 'recipe_add_test.html')

def create_ingredient(request):
    if request.method == "POST":
        name = request.POST['name']
        price = request.POST['price']
        calories = request.POST['calories']
        store = request.POST['store']

        new_ingredient = Ingredient(name=name,price=price,calories=calories,store=store)
        new_ingredient.save()

        return HttpResponse('New Ingredient Created Successfully!')