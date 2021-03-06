from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserCreateForm, CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    add_form = CustomUserCreateForm
    form = CustomUserChangeForm
    list_display = ['username','email','age','is_staff',]
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('age',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)