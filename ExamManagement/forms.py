from django import forms
from .models import Exam


class AddExamForm(forms.Form):
    exam_title = forms.CharField()
    exam_code = forms.IntegerField()
    exam_marks = forms.IntegerField()
    #exam_datetime = forms.DateTimeField()
    exam_duration = forms.IntegerField()

    class Meta:
        model = Exam
        fields = [
            'exam_title',
            'exam_code',
            'exam_datetime',
            'exam_marks',
            'exam_duration',
        ]

    def clean(self):
        return super(AddExamForm, self).clean()
