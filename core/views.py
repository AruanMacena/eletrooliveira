from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


def index_eletro(request):
    return render(request,'index.html')
