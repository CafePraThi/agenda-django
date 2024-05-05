
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from contact.models import Contact
from contact.forms import ContactForm



def create(requests):
  form_action = reverse('contact:create')

  if requests.method == 'POST':
    form = ContactForm(requests.POST)

    context = {
      'form': form,
      'form_action': form_action,
    }

    if form.is_valid():
      contact = form.save()
      return redirect('contact:update', contact_id=contact.pk)

    return render(
      requests,
      'contact/create.html',
      context
    )

  context = {
    'form': ContactForm(),
    'form_action': form_action,
  }

  return render(
    requests,
    'contact/create.html',
    context
  )


def update(requests, contact_id):
  contact = get_object_or_404(Contact, pk=contact_id, show=True)
  form_action = reverse('contact:update', args=(contact_id,))

  if requests.method == 'POST':
    form = ContactForm(requests.POST, instance=contact)

    context = {
      'form': form,
      'form_action': form_action,
    }

    if form.is_valid():
      contact = form.save()
      return redirect('contact:update', contact_id=contact.pk)

    return render(
      requests,
      'contact/create.html',
      context
    )

  context = {
    'form': ContactForm(instance=contact),
    'form_action': form_action,
  }

  return render(
    requests,
    'contact/create.html',
    context
  )


def delete(requests, contact_id):
  contact = get_object_or_404(Contact, pk=contact_id, show=True)

  confirmation = requests.POST.get('confirmation', 'no')
  print(confirmation)

  if confirmation == 'yes':
    contact.delete()
    return redirect('contact:index')

  return render(requests, 'contact/contact.html',
                {
                  'contact': contact,
                  'confirmation': confirmation,
                }
                )