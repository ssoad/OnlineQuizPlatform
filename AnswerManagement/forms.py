from django import forms
from .models import Answer, ExamineeCustomAnswer


class InsertAnswerForm(forms.ModelForm):
    answer = forms.FileField(label='Answer Script')
    class Meta:
        model = ExamineeCustomAnswer
        fields = ['answer']
