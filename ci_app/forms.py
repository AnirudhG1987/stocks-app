from django import forms

#custom validator


class FormName(forms.Form):
    ci_script=forms.CharField(widget=forms.TextInput)
    ci_living=forms.CharField(widget=forms.TextInput)
    amount = forms.CharField(widget=forms.NumberInput)
