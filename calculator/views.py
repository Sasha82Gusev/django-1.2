from django.shortcuts import render
import copy

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


def omlet(request):
    DATAOMLET = copy.deepcopy(DATA)
    servings = int(request.GET.get("servings"))
    for x in DATA['omlet']:
        DATAOMLET['omlet'][x] = DATA['omlet'][x]*servings
    context = {
        'recipe': DATAOMLET['omlet']
    }
    return render(request, 'calculator/index.html', context)


def pasta(request):
    DATAPASTA = copy.deepcopy(DATA)
    servings = int(request.GET.get("servings"))
    for x in DATA['pasta']:
        DATAPASTA['pasta'][x] = DATA['pasta'][x]*servings
    context = {
        'recipe': DATAPASTA['pasta']
    }
    return render(request, 'calculator/index.html', context)


def buter(request):
    DATABUTER = copy.deepcopy(DATA)
    servings = int(request.GET.get("servings"))
    for x in DATA['buter']:
        DATABUTER['buter'][x] = DATA['buter'][x]*servings
    context = {
        'recipe': DATABUTER['buter']
    }
    return render(request, 'calculator/index.html', context)