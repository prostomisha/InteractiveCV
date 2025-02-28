from django import template
from aboutMe.models import Question, Choice
import random


register = template.Library()


@register.simple_tag(name='latest_question_list1')
def get_questions():
    # shuffle questions
    questions = list(Question.objects.all())
    random.shuffle(questions)
    # shuffle answers
    for question in questions:
        choices = list(question.choice_set.all())
        random.shuffle(choices)
        question.shuffled_choices = choices
    return questions
