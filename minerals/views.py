from django.shortcuts import render, get_object_or_404
from minerals.models import Mineral


def index(request, initial=''):
    if not initial:
        minerals_list = Mineral.objects.filter(name__startswith='A')
    else:
        minerals_list = Mineral.objects.filter(name__startswith=initial)
    return render(request, 'minerals/index.html',
                  {"minerals": minerals_list,
                   "l_selected": initial})


def course_detail(request, pk):
    mineral = get_object_or_404(Mineral, pk=pk)
    return render(request, 'minerals/mineral_detail.html', {'mineral': mineral.__dict__, 'mineral_obj': mineral, 'l_selected': 'B'})
