from django.shortcuts import render
from minerals.models import Mineral


def index(request):
    minerals_list = Mineral.objects.all()
    return render(request, 'minerals/index.html', {"minerals": minerals_list})
