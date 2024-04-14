# myapp/admin.py
from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    # Customize the display fields in the change list page
    list_display = ('name', 'email', 'message','created_at')

    # Add any other customizations as needed

# Register your model with the custom ModelAdmin
admin.site.register(Contact, ContactAdmin)
