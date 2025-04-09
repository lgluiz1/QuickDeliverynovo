from django.db import models

# Create your models here.

class SiteConfig(models.Model):
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    video_principal = models.FileField(upload_to='videos/', blank=True, null=True)
    video_viagens = models.FileField(upload_to='videos/', blank=True, null=True)

    imagens = models.ImageField(upload_to='imagens/', blank=True, null=True)

    imagen_png = models.ImageField(upload_to='imagens/', blank=True, null=True)
    def __str__(self):
        return "Configuração do Site"
    
class RedesSociais(models.Model):
    facebook = models.CharField(max_length=100, blank=True)
    instagram = models.CharField(max_length=100, blank=True)
    youtube = models.CharField(max_length=100, blank=True)
    x = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Redes Sociais #{self.id}"

class Telefone(models.Model):
    redes_sociais = models.ForeignKey(RedesSociais, on_delete=models.CASCADE, related_name='telefones')
    numero = models.CharField(max_length=20)

    def __str__(self):
        return self.numero

class Email(models.Model):
    redes_sociais = models.ForeignKey(RedesSociais, on_delete=models.CASCADE, related_name='emails')
    endereco = models.EmailField()

    def __str__(self):
        return self.endereco
    
# link Video 
class VideoSobre(models.Model):
    url_video = models.URLField(verbose_name="Link do YouTube")
    data_adicionado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url_video

class CodEtica(models.Model):
    # carregar PDF
    pdf = models.FileField(upload_to='cod_etica/', blank=True, null=True)

    def __str__(self):
        return "Cod Etica"