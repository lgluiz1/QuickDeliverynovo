from django.shortcuts import render, redirect

# Create your views here.
from django.contrib import messages
from core.forms import CotacaoForm, MedidaForm
from core.views import index
from django.forms import formset_factory

def cotacao_view(request):
    MedidaFormSet = formset_factory(MedidaForm, extra=1)

    if request.method == 'POST':
        cotacao_form = CotacaoForm(request.POST)
        medida_formset = MedidaFormSet(request.POST, prefix='medidas')

        if cotacao_form.is_valid() and medida_formset.is_valid():
            # Aqui você salva os dados
            print(cotacao_form.cleaned_data)
            for form in medida_formset:
                print(form.cleaned_data)
            # redirecionar ou mostrar confirmação

    else:
        cotacao_form = CotacaoForm()
        medida_formset = MedidaFormSet(prefix='medidas')

    context = {
        'form': cotacao_form,
        'formset': medida_formset,
        
    }
    return render(request, "modal/modalcotacao.html", context)