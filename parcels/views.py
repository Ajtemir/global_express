from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class ParcelsView(LoginRequiredMixin, TemplateView):
    template_name = 'parcels/parcels.html'
    login_url = '/sign/'
