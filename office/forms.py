from django import forms
from office.models import Department

class DeptForm(forms.ModelForm):
    class Meta:
        model=Department
        fields="__all__"