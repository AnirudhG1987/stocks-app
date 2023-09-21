from django import forms

#custom validator


class FormName(forms.Form):
    int_script=forms.CharField(widget=forms.TextInput)
    inv_script = forms.CharField(widget=forms.TextInput)
    living_growth_script=forms.CharField(widget=forms.TextInput)
    initial_investment_amount = forms.CharField(widget=forms.NumberInput)
    initial_borrowing_amount = forms.CharField(widget=forms.NumberInput)
    initial_living_amount = forms.CharField(widget=forms.NumberInput)
