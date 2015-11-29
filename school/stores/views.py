#c51162
from django.shortcuts import render
from models import *
from common.models import *
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView

class IndexView(TemplateView):
	template_name = 'stores/index.html'
