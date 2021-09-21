from django.shortcuts import render, redirect
from .forms import PredioForm

# Create your views here.
def Home(request):
    return render(request, 'cuentas/index.html')

def registrarPredio(request):
    if request.method == 'POST':
        predio_form = PredioForm(request.POST)
        if predio_form.is_valid():
            predio_form.save()
            return redirect('../')
    else:
        predio_form = PredioForm()
    return render(request, 'cuentas/registrarpredio.html', {'predio_form':predio_form})