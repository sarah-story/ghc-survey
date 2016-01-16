from django.shortcuts import render
from django.http import HttpResponse
import forms


def index(request):
    if request.method == 'GET':
        first_form = forms.PrelimQuestions()
    return render(request, 'page_one.html', {
        'form': first_form,
    })
