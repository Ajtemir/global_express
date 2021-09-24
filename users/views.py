from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import FormView

from users.forms import SignForm


class RegistrationView(FormView):
    ...


class SignView(FormView):

    template_name = 'users/sign.html'
    success_url = '/'
    form_class = SignForm

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))





