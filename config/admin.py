from django.contrib import admin
from .models import SiteConfig , Telefone , RedesSociais , Email, VideoSobre

# Register your models here.
admin.site.register(SiteConfig)
admin.site.register(VideoSobre)

class TelefoneInline(admin.TabularInline):  # ou admin.StackedInline se preferir
    model = Telefone
    extra = 1  # mostra um campo a mais para adicionar novo telefone

class EmailInline(admin.TabularInline):
    model = Email
    extra = 1


@admin.register(RedesSociais)
class RedesSociaisAdmin(admin.ModelAdmin):
    inlines = [TelefoneInline, EmailInline]
