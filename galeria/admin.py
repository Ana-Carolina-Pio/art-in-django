from django.contrib import admin

from galeria.models import Artista
from galeria.models import Arte

# Register your models here.
class ArtistaAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


class ArtAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(Artista, ArtistaAdmin)
admin.site.register(Arte, ArtAdmin)