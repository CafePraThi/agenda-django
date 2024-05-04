
from django.shortcuts import render

from contact.forms import ContactForm



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