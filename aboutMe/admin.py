from django.contrib import admin

from .models import Question, UserQuestion, UserChoice
from .models import Choice


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_text',)
    list_display_links = ('id', 'question_text',)


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'choice_text', 'question', 'check_choice')
    list_display_links = ('id', 'choice_text',)


class UserQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_text', 'used_in_main_questions')
    list_display_links = ('id', 'question_text',)


class UserChoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'choice_text', 'question', 'check_choice')
    list_display_links = ('id', 'choice_text',)


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(UserQuestion, UserQuestionAdmin)
admin.site.register(UserChoice, UserChoiceAdmin)
