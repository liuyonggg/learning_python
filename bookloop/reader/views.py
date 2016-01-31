from django.shortcuts import render
from django.contrib import admin
from django.utils.translation import ugettext as _, ugettext_lazy
from django.views.generic import TemplateView

# Create your views here.

class IndexView(TemplateView):
    template_name = "reader/index.html"

    def get_context_data(self, **kwargs):
        return {'user': self.request.user}



