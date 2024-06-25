from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import User


class CustomUserAdmin(UserAdmin):
    model = User
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'date_joined', 'last_login')}),
    )
    # extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}


admin.site.unregister(Group)
admin.site.register(User, CustomUserAdmin)
