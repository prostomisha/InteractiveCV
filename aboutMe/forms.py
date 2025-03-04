from django import forms
from .models import UserQuestion, UserChoice


class UserQuestionForm(forms.ModelForm):
    class Meta:
        model = UserQuestion
        fields = ('question_text',)
        widgets = {
            'question_text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Question'}),
        }


class UserChoiceForm(forms.ModelForm):
    class Meta:
        model = UserChoice
        fields = ('choice_text', 'check_choice')
