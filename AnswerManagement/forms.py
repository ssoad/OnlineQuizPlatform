from django import forms
from .models import Answer, ExamineeAnswer


class InsertAnswerForm(forms.ModelForm):
    answer = forms.FileField(label='Answer Script')
    class Meta:
        model = ExamineeAnswer
        fields = ['answer']
