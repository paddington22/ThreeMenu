from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class MenuTemplateView(TemplateView):
    template_name = 'menu/index.html'
