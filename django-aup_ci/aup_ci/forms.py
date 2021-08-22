from django import forms
class ContactForm(forms.Form):
    lastname = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Nom*', 'class': 'check-form'}))
    firstname = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Prenom(s)*', 'class': 'check-form'}))
    email = forms.CharField(label='', widget=forms.EmailInput(attrs={'placeholder': 'Email*', 'class': 'check-form'}))
    phone = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Téléphone*', 'class': 'check-form'}))
    message = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Préoccupation*'}))

