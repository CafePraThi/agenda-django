from django.shortcuts import render
from contact.models import Contact
# Create your views here.

def index(requests):

  contacts = Contact.objects.filter(show=True).order_by('-id')

  context = {
    'contacts': contacts,
  }

  return render(
    requests,
    'contact/index.html',
    context
  )