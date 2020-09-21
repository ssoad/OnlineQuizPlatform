from django import forms
from .models import Answer

class insertAnswerform(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('corr_ans','question')

