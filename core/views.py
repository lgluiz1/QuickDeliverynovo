from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from config.models import SiteConfig , RedesSociais, Telefone, Email, VideoSobre  # Agora vem do app config
from core.forms import CotacaoForm, MedidaForm
from django.forms import formset_factory

def index(request):
    config = SiteConfig.objects.first()
    redes = RedesSociais.objects.first()
    video_yt= VideoSobre.objects.first()
    telefones = redes.telefones.all() if redes else []
    emails = redes.emails.all() if redes else []

    MedidaFormSet = formset_factory(MedidaForm, extra=1)

    if request.method == 'POST':
        cotacao_form = CotacaoForm(request.POST)
        medida_formset = MedidaFormSet(request.POST, prefix='medidas')

        if cotacao_form.is_valid() and medida_formset.is_valid():
            # Salvar os dados
            print(cotacao_form.cleaned_data)
            for form in medida_formset:
                print(form.cleaned_data)
            # Aqui você pode salvar no banco ou redirecionar
            # return redirect('alguma_view_de_confirmacao')

    else:
        cotacao_form = CotacaoForm()
        medida_formset = MedidaFormSet(prefix='medidas')

    context = {
        'form': cotacao_form,
        'formset': medida_formset,
        'config': config,
        'emails': emails,
        'redes': redes,
        'telefones': telefones,
        'yt': video_yt,
    }
    return render(request, 'core/home.html', context)
