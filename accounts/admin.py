from django.contrib import admin
from .models import CustomUser

# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            'Personal',{
                'fields':(
                    'first_name', 'last_name'
                ),
            }
        ),
        (
            'Credentials', {
                'fields': ('email', 'password')
            }
        ),
    )
