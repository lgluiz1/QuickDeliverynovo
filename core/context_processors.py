from config.models import SiteConfig, RedesSociais, VideoSobre, CodEtica
from core.forms import CotacaoForm, MedidaForm
from django.forms import formset_factory

def dados_globais(request):
    config = SiteConfig.objects.first()
    redes = RedesSociais.objects.first()
    video_yt = VideoSobre.objects.first()
    pdf_cod_etica = CodEtica.objects.first()
    telefones = redes.telefones.all() if redes else []
    emails = redes.emails.all() if redes else []

    # Formulários
    MedidaFormSet = formset_factory(MedidaForm, extra=1)

    cotacao_form = CotacaoForm()
    medida_formset = MedidaFormSet(prefix='medidas')

    return {
        'config': config,
        'redes': redes,
        'yt': video_yt,
        'telefones': telefones,
        'emails': emails,
        'form': cotacao_form,
        'formset': medida_formset,
    }
