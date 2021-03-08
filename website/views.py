from django.shortcuts import render
from .models import Question
from django.shortcuts import render, get_object_or_404

def question_list(request):
        questions = Question.objects.all()
        return render(request, 'website/question_list.html', {'questions' : questions})

def question_detail(request, pk):
        question = get_object_or_404(Question, pk=pk)
        return render(request, 'website/question_detail.html', {'question': question})
