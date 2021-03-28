from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account
from django.utils.translation import gettext, gettext_lazy as _
# Register your models here.

@admin.register(Account)
class UserAdmin(UserAdmin):
    list_display= ["name","username","user_type","okul",'sinif']
    search_fields= ["name"]
    readonly_fields=['date_joined','last_login']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('name', 'user_type', 'email','okul','sinif')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    autocomplete_fields = ['okul','sinif']