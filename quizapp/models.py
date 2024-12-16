from django.db import models

# Create your models here.
class Questions(models.Model):
    question_text = models.CharField(max_length=255)
    option_a = models.CharField(max_length=100)
    option_b = models.CharField(max_length=100)
    option_c = models.CharField(max_length=100)
    option_d = models.CharField(max_length=100)
    correct_answer = models.CharField(max_length=100)  # 'A', 'B', 'C', or 'D'

    def __str__(self):
        return self.question_text

class QuizSession(models.Model):
    total_questions = models.IntegerField(default=0)
    correct_answers = models.IntegerField(default=0)
    incorrect_answers = models.IntegerField(default=0)

    def __str__(self):
        return f"Session {self.id} - Correct: {self.correct_answers}, Incorrect: {self.incorrect_answers}"
