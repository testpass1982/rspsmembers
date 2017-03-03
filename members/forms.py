from django import forms
from .models import RspsMember

class MemberForm(forms.ModelForm):
    class Meta:
        model = RspsMember
        fields = ('last_name', 'first_name', 'middle_name',)
