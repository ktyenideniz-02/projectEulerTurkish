from django.shortcuts import render
from .models import Question

def question_list(request):
        questions = Question.objects.all()
        return render(request, 'website/question_list.html', {'questions' : questions})
