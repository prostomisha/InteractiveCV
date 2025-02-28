from datetime import timezone

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Question, Choice


def index(request):
    latest_question_list = Question.objects.all()
    context = {"latest_question_list": latest_question_list}
    return render(request, "aboutMe/index.html", context)


def test_yourself(request):
    #latest_question_list = Question.objects.all()
    #context = {"latest_question_list": latest_question_list}

    return render(request, "aboutMe/test_yourself.html")


def check_answers(request):
    if request.method == "POST":
        correct_count = 0  # Counter for correct answers
        correct_choices = {}  # Dict { question_id: correct_choice_id }
        all_questions = len(Question.objects.all())

        for question in Question.objects.all():
            correct_choice = question.choice_set.filter(check_choice=True).first()
            if correct_choice:
                correct_choices[question.id] = correct_choice.id

        user_answers = {}  # { question_id: selected_choice_id }

        for key, value in request.POST.items():
            if key.startswith("question_"):  # Фильтруем только ответы
                question_id = int(key.split("_")[1])  # Получаем ID вопроса
                choice_id = int(value)  # ID выбранного ответа
                user_answers[question_id] = choice_id

                if choice_id == correct_choices.get(question_id):
                    correct_count += 1  # Увеличиваем счетчик правильных ответов

        return JsonResponse({
            "correct_answers": correct_count,
            "correct_choices": correct_choices,  # Передаем правильные ответы
            "user_answers": user_answers,  # Передаем, что выбрал пользователь
            "all_questions": all_questions,
        })

    return JsonResponse({"error": "Invalid request"}, status=400)


def resume(request):
    context = {}
    return render(request, "aboutMe/resume.html", context)