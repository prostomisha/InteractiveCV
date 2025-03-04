from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    check_choice = models.BooleanField(default=False)


class UserQuestion(models.Model):
    question_text = models.CharField(max_length=200)
    used_in_main_questions = models.BooleanField(default=False)

    def __str__(self):
        return self.question_text

    def get_absolute_url(self):
        return 'test_yourself'


class UserChoice(models.Model):
    question = models.ForeignKey(UserQuestion, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    check_choice = models.BooleanField(default=False)
