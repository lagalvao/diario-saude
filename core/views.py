from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserModelForm, UserUpdateForm, formControle, formHistorico, formAnalise
from .models import Controle, Remedio, Analise, Historico
from django.contrib.auth.models import User
from django.db.models import Q


# Criacao de views
def home(request):
    return render(request, 'home.html')


def visitante(request):
    return render(request, 'visitante.html')


@login_required
def painel(request):
    us = request.user.id
    click = Analise.objects.filter(usuario__icontains=us).values_list('remedio', flat=True)
    click2 = Historico.objects.filter(usuario__icontains=us).values_list('remedio', flat=True)
    obj = Remedio.objects.filter(id__in=click)
    obj2 = Remedio.objects.filter(id__in=click2)

    context = {
        "obj": obj,
        "obj2": obj2
    }
    return render(request, 'painel.html', context)


@login_required
def agenda(request):
    us = request.user.id
    obj = Controle.objects.filter(usuario__icontains=us)
    context = {
        "obj": obj
    }
    return render(request, 'agenda.html', context)


def registroUsuario(request):
    form = UserModelForm(request.POST or None)
    context = {'form': form}
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, "cadastro.html", context)


@login_required
def editarUsuario(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('painel')
    else:
        form = UserUpdateForm(instance=request.user)
        args = {'form': form}
        return render(request, 'perfil.html', args)


@login_required
def insereAgenda(request):
    form = formControle(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('agenda')
    context = {'form': form}
    return render(request, 'cadAgenda.html', context)


@login_required
def buscaMed(request):
    obj = Remedio.objects.all()

    query = request.GET.get('pesquisa')
    if query:
        obj = Remedio.objects.filter(nome_cientifico__icontains=query)

    context = {
        'obj':obj

    }
    return render(request, 'busca.html', context)


@login_required
def cadAnalise(request):
    form = formAnalise(request.POST or None)
    form2 = formHistorico(request.POST or None)
    context = {'form': form, 'form2': form2}
    if request.method == "POST":
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return redirect('buscaMed')
    return render(request, 'teste.html', context)


@login_required
def exAnalise(request):
    us = request.user.id
    obj = Analise.objects.filter(usuario__icontains=us).delete()

    context = {
        "obj": obj
    }
    return redirect('painel')