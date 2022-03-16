from django.shortcuts import render
from django.views.generic import TemplateView
from .stats import get_stats

# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_shootings'] = get_stats()
        return context