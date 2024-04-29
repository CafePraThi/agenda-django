from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.

def index(requests):
  contacts = Contact.objects.filter(show=True).order_by('-id')

  paginator = Paginator(contacts, 10)
  page_number = requests.GET.get("page")
  page_obj = paginator.get_page(page_number)

  context = {
    'page_obj': page_obj,
    'site_title': 'Contatos - ',
  }

  return render(
    requests,
    'contact/index.html',
    context
  )

def search(requests):
  search_value = requests.GET.get('q', '').strip()

  if search_value == '':
    return redirect('contact:index')

  contacts = Contact.objects \
    .filter(show=True) \
    .filter(
      Q(first_name__icontains=search_value) |
      Q(last_name__icontains=search_value) |
      Q(phone__icontains=search_value) |
      Q(email__icontains=search_value)
      ) \
    .order_by('-id')
  
  paginator = Paginator(contacts, 10)
  page_number = requests.GET.get("page")
  page_obj = paginator.get_page(page_number)

  context = {
    'page_obj': page_obj,
    'site_title': 'Contatos - ',
  }

  return render(
    requests,
    'contact/index.html',
    context
  )

def contact(requests, contact_id):
  #single_contact = Contact.objects.filter(id=contact_id).first()
  single_contact = get_object_or_404(Contact.objects.filter(id=contact_id, show=True))

  site_title = f'{single_contact.first_name} {single_contact.last_name} - '

  context = {
    'contact': single_contact,
    'site_title': site_title,
  }

  return render(
    requests,
    'contact/contact.html',
    context
  )