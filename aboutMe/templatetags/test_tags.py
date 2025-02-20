from django import template
from aboutMe.models import Question, Choice
import random


register = template.Library()


@register.simple_tag(name='latest_question_list1')
def get_questions():
    questions = list(Question.objects.all())
    random.shuffle(questions)
    return questions
