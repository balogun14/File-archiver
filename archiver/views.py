# from django.shortcuts import render
from django.views.generic import ListView

from .models import Archiver

# Create your views here.


class ArchiverListView(ListView):
    model = Archiver
    template_name = "base.html"
