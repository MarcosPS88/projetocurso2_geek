from django.shortcuts import render, redirect
from .forms import ContatoForm, ProdutoModelForm
from django.contrib import messages
from .models import Produto
from  django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required


def index(request):
    context = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'index.html', context)


def contato(request):
    form = ContatoForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.send_mail()
            messages.success(request, 'E-mail enviado com sucesso')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar e-mail')

    context = {
        'form': form
    }
    return render(request=request,
                  template_name='contato.html',
                  context=context)


@login_required(login_url='login')
def produto(request):
    user = request.user
    if str(user) != 'AnonymousUser':

        if request.method == 'POST':
            form = ProdutoModelForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Produto salvo com Sucesso')
                form = ProdutoModelForm()
            else:
                messages.error(request, 'Erro ao salvar produto.')
        else:
            form = ProdutoModelForm()
        context = {
            'form': form
        }
        return render(request, 'produto.html', context)

    return render(request, 'login.html')


def login(request):
    form = AuthenticationForm(request)
    context = {'form': form}
    if request.method == 'POST':
        form = AuthenticationForm(
                              request,
                              data=request.POST
                             )
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Logado com sucesso!')
            return redirect('produto')
        else:
            messages.error(request, 'Login inválido')
            return render(request, 'login.html', context)
    else:

        return render(request, 'login.html', context)


@login_required(login_url='login')
def logout(request):
    if str(request.user) != 'AnonymousUser':
        auth.logout(request=request)
    return redirect('login')
