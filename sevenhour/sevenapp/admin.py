# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import User


# class CustomUserAdmin(UserAdmin):
#     model = User
#     list_display = ['username','id', 'email', 'is_staff', 'is_superuser']  # Adjust field names here
#     fieldsets = (
#         (None, {'fields': ('username', 'password')}),
#         ('Personal info', {'fields': ('email',)}),
#         ('Permissions', {'fields': ('is_staff', 'is_superuser', 'is_active')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('username', 'password1', 'password2', 'is_staff', 'is_superuser', 'is_active')}
#         ),
#     )
#     search_fields = ('username', 'email')  # Adjust field names here
#     ordering = ('username',)  # Adjust field names here

# admin.site.register(User, CustomUserAdmin)

from django.contrib import admin
# from django.contrib.auth.models import User

# admin.site.register(User)

