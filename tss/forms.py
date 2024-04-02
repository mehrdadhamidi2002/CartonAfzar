from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

    def save(self, commit=True):
        contact = super().save(commit=False)
        # Perform any additional processing or validation here
        if commit:
            contact.save()
        return contact