from typing import Any
from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator
from django import forms
from django.core.exceptions import ValidationError

from contact.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'first_name', 'last_name', 'phone',
        )
    def clean(self):
        cleaned_data = self.cleaned_data
        self.add_error('first_name', ValidationError('Mensagem de erro', code='invalid'))
        return super().clean()


def create(requests):
  if requests.method == 'POST':
    context = {
    'form': ContactForm(requests.POST)
  }

    return render(
      requests,
      'contact/create.html',
      context
    )

  context = {
    'form': ContactForm()
  }

  return render(
    requests,
    'contact/create.html',
    context
  )