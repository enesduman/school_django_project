from django.contrib import admin
from .models import Sinif


@admin.register(Sinif)
class SinifAdmin(admin.ModelAdmin):
    list_display= ["adi"]
    list_display_links= ["adi"]
    search_fields= ["adi"]
    class Meta:
        model = Sinif