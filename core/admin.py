from django.contrib import admin
from .models import Produto


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome',
                    'preco',
                    'estoque',
                    'slug',
                    'criado',
                    'modificado',
                    'ativo'
                    )


admin.site.register(Produto, ProdutoAdmin)  # ou usar o decorator @admin.register(nomedaclasse)
