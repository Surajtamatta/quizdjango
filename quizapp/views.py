from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Questions, QuizSession
import random

def quiz_start(request):
    session = QuizSession.objects.create(total_questions=0, correct_answers=0, incorrect_answers=0)
    return redirect('get_question', session_id=session.id)

def get_question(request, session_id):
    session = get_object_or_404(QuizSession, id=session_id)
    question = Questions.objects.order_by('?').first()

    if not question:
        return render(request, 'no_question.html')
    session.total_questions += 1
    session.save()

    return render(request, 'question.html', {'question': question, 'session_id': session.id})

def submit_answer(request, session_id, question_id):
    session = get_object_or_404(QuizSession, id=session_id)
    question = get_object_or_404(Questions, id=question_id)

    user_answer = request.POST.get('answer')
    print(user_answer, question.correct_answer)
    if user_answer == question.correct_answer:
        result = 'Correct'
        session.correct_answers += 1
    else:
        result = 'Incorrect'
        session.incorrect_answers += 1

    session.save()
     
    return render(request, 'result.html', {
        'result': result,
        'question': question,
        'session_id': session.id
    })

def quiz_results(request, session_id):
    session = get_object_or_404(QuizSession, id=session_id)

    return render(request, 'summary.html', {
        'session': session
    })


