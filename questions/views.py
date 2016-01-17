from django.shortcuts import render, redirect
from django.http import HttpResponse
from models import Person
import forms


def index(request):
    if request.method == 'POST':
        form = forms.PrelimQuestions(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            person = Person()
            person.street_address = data.get('street_address')
            person.city = data.get('city')
            person.zip = data.get('zip')
            person.status = data.get('status')
            person.save()
            return redirect('page_two', person=person)
    else:
        form = forms.PrelimQuestions()
    return render(request, 'page_one.html', {
        'form': form,
    })


def page_two(request, person):
    return HttpResponse(person.street_address)


def success(request):
    return


def page_three(request):
    return
