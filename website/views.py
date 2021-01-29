from django.shortcuts import render

def question_list(request):
    return render(request, 'website/question_list.html', {})
