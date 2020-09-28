from django import forms
from .models import Answer, ExamineeCustomAnswer


class InsertAnswerForm(forms.ModelForm):
    class Meta:
        model = ExamineeCustomAnswer
        fields = '__all__'
