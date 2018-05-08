from django.shortcuts import render, get_object_or_404
from minerals.models import Mineral


def index(request):
    minerals_list = Mineral.objects.all()
    return render(request, 'minerals/index.html', {"minerals": minerals_list})


def course_detail(request, pk):
    mineral = get_object_or_404(Mineral, pk=pk)
    return render(request, 'minerals/mineral_detail.html', {'mineral': mineral})
