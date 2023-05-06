from django import forms
from .models import UserDetails

materials_choices = (
    ('debit', 'Debit Card'),
    ('credit', 'Credit Card'),
    ('cheque', 'Cheque Book'),
)


class UserDetailsForm(forms.ModelForm):
    materials = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), choices=materials_choices)

    class Meta:
        model = UserDetails
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'dob': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'Email': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
            'account_type': forms.Select(attrs={'class': 'form-control'}),
            'materials': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'})
        }
