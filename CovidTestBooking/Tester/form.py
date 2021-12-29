from django import forms
from Tester import models
from Tester.models import user


class Myform(forms.ModelForm):
    class Meta:
        model = user
        fields = []
