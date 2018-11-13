# -*- coding: utf-8 -*-
from django import forms
from .models import Email


class EmailForm(forms.ModelForm):
    u"""Formularz email"""

    class Meta:
        model = Email
        fields = ['title', 'message', 'recipient']
