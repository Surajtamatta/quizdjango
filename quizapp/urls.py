from django.urls import path
from . import views

urlpatterns = [
    path('start/', views.quiz_start, name='quiz_start'),
    path('<int:session_id>/question/', views.get_question, name='get_question'),
    path('<int:session_id>/submit/<int:question_id>/', views.submit_answer, name='submit_answer'),
    path('<int:session_id>/result/', views.quiz_results, name='quiz_results'),

]
