from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>This is the testing platform</h1>")
def detail(request, question_id):
    return  HttpResponse("<h2> Question" + str(question_id) + "</h2>")