from django.shortcuts import render
from .forms import ContatoForm
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def contato(request):
    form = ContatoForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']
            print('Mensagem enviada')
            print(nome)
            print(email)
            print(assunto)
            print(mensagem)
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


def produto(request):
    return render(request, 'produto.html')

