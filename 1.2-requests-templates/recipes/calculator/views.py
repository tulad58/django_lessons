from django.shortcuts import render, reverse
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
def index(request):
    template_name = 'calculator/index.html'

    return render(request, template_name, context)

def omlet_view(request):
    template_name = 'calculator/index.html'
    context = {
      'recipe': {
          'яйца, шт': 2,
          'молоко, л': 0.1,
          'соль, ч.л.': 0.5,
      }
    }
    return render(request, template_name, context)

def pasta_view(request):
    template_name = 'calculator/index.html'
    context = {
      'recipe': {
          'макароны, г': 0.3,
          'сыр, г': 0.05,
      }
    }
    return render(request, template_name, context)

def buter_view(request):
    template_name = 'calculator/index.html'
    context = {
      'recipe': {
          'хлеб, ломтик': 1,
          'колбаса, ломтик': 1,
          'сыр, ломтик': 1,
          'помидор, ломтик': 1,
      }
    }
    return render(request, template_name, context)
