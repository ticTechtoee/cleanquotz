from django import forms

class EmailForm(forms.Form):
    recipient = forms.EmailField()
    first_name = forms.CharField(max_length=15)
    message = forms.CharField(widget=forms.Textarea)