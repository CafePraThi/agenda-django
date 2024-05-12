from django.shortcuts import render, redirect
from contact.forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

def register(request):
  form = RegisterForm()

  if request.method == 'PSOT':
    form = RegisterForm(request.POST)

    if form.is_valid():
      form.save()
      messages.success(request, 'Cadastrado com Sucesso!')
      return redirect('contact:login')

  return render(request, 'contact/register.html',
                {
                  'form': form,
                })


def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
       form = AuthenticationForm(request, data=request.POST)

       if form.is_valid():
          user = form.get_user()
          auth.login(request, user)
          messages.success(request, 'Logado com sucesso')
          return redirect('contact:index')


    return render(request, 'contact/login.html',
                {
                  'form': form,
                })

def logout_view(request):
   auth.logout(request)
   return redirect('contact:login')