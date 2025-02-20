from datetime import timezone

from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice


def index(request):
    latest_question_list = Question.objects.all()
    context = {"latest_question_list": latest_question_list}
    return render(request, "aboutMe/index.html", context)


def test_yourself(request):
    #latest_question_list = Question.objects.all()
    #context = {"latest_question_list": latest_question_list}
    questions = list(Question.objects.all())
    if request.method == "POST":
        correct_count = 0
        total_questions = len(questions)

        for question in questions:
            selected_choice_id = request.POST.get(f"question_{question.id}")
            if selected_choice_id:
                choice = Choice.objects.get(id=int(selected_choice_id))
                if choice.check_choice:
                    correct_count += 1

        return render(request, "aboutMe/test_yourself.html", {
            "result": f"You answered correctly on {correct_count} from {total_questions} questions!"
        })
    return render(request, "aboutMe/test_yourself.html")


def resume(request):
    context = {}
    return render(request, "aboutMe/resume.html", context)