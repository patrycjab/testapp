from django.http import HttpResponseRedirect
from django.views.generic import FormView

from .forms import EmailForm
from .tasks import save_email


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
