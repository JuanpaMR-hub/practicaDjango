from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Persona
from . import forms


def home(request):
    if request.method == 'POST':
        if 'save' in request.POST:
            form = forms.PersonaForm(request.POST)
            if form.is_valid():
                form.save()
                
        elif 'delete' in request.POST:
                pk = request.POST.get('delete')
                Persona.objects.get(pk = pk).delete()

        return HttpResponseRedirect(request.path_info)

    personas = Persona.objects.all()
    form = forms.PersonaForm()
    return render(request,'home.html',{'personas':personas, 'form':form})
