from django.shortcuts import render

# Create your views here.
from django.views.generic import *
from .models import *

class HomeView(TemplateView):
    template_name = 'clienttemplates/home.html'