from django.shortcuts import render, get_object_or_404
from minerals.models import Mineral


def index(request, initial=''):
    print("IP Address for debug-toolbar: " + request.META['REMOTE_ADDR'])
    if not initial:
        minerals_list = Mineral.objects.filter(name__startswith='A')
        initial = 'A'
    else:
        minerals_list = Mineral.objects.filter(name__startswith=initial)
    return render(request, 'minerals/index.html',
                  {"minerals": minerals_list,
                   "l_selected": initial})


def minerals_group(request, group):
    g_name = group.replace('_', ' ')
    minerals_list = Mineral.objects.filter(group=g_name)
    return render(request, 'minerals/index.html', {"minerals": minerals_list, 'g_selected': group})


def mineral_detail(request, pk):
    mineral = get_object_or_404(Mineral, pk=pk)
    return render(request, 'minerals/mineral_detail.html',
                  {'mineral': mineral.__dict__, 'mineral_obj': mineral})


def search(request):
    term = request.GET.get('q')
    minerals_list = Mineral.objects.filter(name__icontains=term)
    return render(request, 'minerals/index.html', {"minerals": minerals_list})
