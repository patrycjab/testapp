from django.shortcuts import render
from django.views.generic import FormView

# Create your views here.

from .tasks import save_email

from .forms import EmailForm


class ViewEmailSend(FormView):
    u"""Widok obsługi formularza EmailForm."""
    template_name = 'email_form.html'
    form_class = EmailForm
    success_url = '/'

    def form_valid(self, form):
        save_email.delay(form)
            import ipdb;ipdb.set_trace()
        return HttpResponseRedirect(self.get_success_url())
