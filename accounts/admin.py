from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Role


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('more information', {'fields': ('phone', 'permission', )}),
    )
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone', 'permission', )}),
    )
    list_display = ('username', 'first_name', 'last_name', 'phone', 'permission', )


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'permission', )
