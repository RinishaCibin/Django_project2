from django import forms


class HomeWorkForm(forms.Form):
    subject=forms.CharField()
    question=forms.CharField()
    submit_date=forms.DateField()