from django import forms

class CotacaoForm(forms.Form):
    nome = forms.CharField(label="Nome", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    empresa = forms.CharField(label="Empresa", max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    celular = forms.CharField(label="Celular", max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefone = forms.CharField(label="Telefone", max_length=20, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="E-mail", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    cnpj_remetente = forms.CharField(label="CNPJ Remetente", max_length=18, widget=forms.TextInput(attrs={'class': 'form-control'}))
    uf_remetente = forms.CharField(label="UF Remetente", max_length=2, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cidade_remetente = forms.CharField(label="Cidade Remetente", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cnpj_destinatario = forms.CharField(label="CNPJ Destinatário", max_length=18, widget=forms.TextInput(attrs={'class': 'form-control'}))
    uf_destinatario = forms.CharField(label="UF Destinatário", max_length=2, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cidade_destinatario = forms.CharField(label="Cidade Destinatário", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    tomador_servico = forms.ChoiceField(
        choices=[("REMETENTE", "Remetente"), ("DESTINATARIO", "Destinatário")],
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Tomador do Serviço"
    )
    
    tipo_carga = forms.CharField(label="Tipo de Carga", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    tipo_embalagem = forms.CharField(label="Tipo de Embalagem", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    peso = forms.FloatField(label="Peso (Kg)", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    valor_mercadoria = forms.DecimalField(label="Valor da Mercadoria", max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    veiculo_especial = forms.ChoiceField(
        choices=[("Sim", "Sim"), ("Não", "Não")],
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Necessita veículo ou equipamento especial?"
    )

class MedidaForm(forms.Form):
    comprimento = forms.CharField(label="Comprimento (cm)", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    largura = forms.CharField(label="Largura (cm)", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    altura = forms.CharField(label="Altura (cm)", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    peso = forms.CharField(label="Peso (Kg)", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
