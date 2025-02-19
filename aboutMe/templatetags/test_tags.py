from django import template
from aboutMe.models import Question, Choice

register = template.Library()


@register.simple_tag(name='latest_question_list1')
def get_questions():
    return Question.objects.all()
