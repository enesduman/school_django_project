from django.contrib import admin

from .models import Okul

@admin.register(Okul)
class OkulAdmin(admin.ModelAdmin):
    list_display= ["adi","il"]
    list_display_links= ["adi","il"]
    search_fields= ["adi"]
    class Meta:
        model = Okul