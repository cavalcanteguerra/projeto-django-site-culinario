from django.shortcuts import render
from utils.recipes import factory


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'recipes': [factory.make_recipe() for _ in range(10)],
    })

def recipes(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': factory.make_recipe(),
        'is_detail_page': True,
    })
