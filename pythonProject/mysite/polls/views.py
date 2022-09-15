from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
# Create your views here.

def index(request):
    myname = "Le Anh Tuan"
    items = ["Phone", "Laptop", "Motobike", "Money"]
    context = {"name": myname, "items": items}
    return render(request, "polls/index.html", context)

# def func1(request):
#     return HttpResponse("<h1>Function 1</h1><p>Hellooo!</p>")

def display_question_list(request):
    question_list = Question.objects.all()
    context = {"question_list": question_list}
    return render(request, "polls/question_list.html", context)

def detailView(request, question_id):
    question = Question.objects.get(pk=question_id)
    return render(request, "polls/detail_question.html", {"question": question})

def vote(request, question_id):
    question = Question.objects.get(pk=question_id)
    try:
        data = request.POST["choice"]
        answer = question.choice_set.get(pk=data)
    except:
        return HttpResponse("Choice is not exist.")
    answer.vote += 1
    answer.save()
    return render(request, 'polls/result.html', {'question': question})