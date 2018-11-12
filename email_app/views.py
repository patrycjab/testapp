from django.shortcuts import render
from django.views.generic import FormView
from django.http import HttpResponseRedirect

# Create your views here.

from .tasks import save_email

from .forms import EmailForm


class ViewEmailSend(FormView):
    u"""Widok obsługi formularza EmailForm."""
    template_name = 'email_form.html'
    form_class = EmailForm
    success_url = '/'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()

        save_email.delay(obj.pk)
        return HttpResponseRedirect(self.get_success_url())
