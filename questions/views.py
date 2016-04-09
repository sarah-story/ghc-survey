from django.shortcuts import render, redirect
from models import Person
import forms




def index(request):
    if request.method == 'POST':
        form = forms.PrelimQuestions(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            person = Person()
            person.street_address = " ".join(data.get('street_address').lower().split())
            person.city = "Nashville"
            person.zip = 37205
            request.session['current_person'] = person
            return redirect('address_visited')
    else:
        form = forms.PrelimQuestions()
    return render(request, 'page_one.html', {
        'form': form,
    })


def address_visited(request):
    person = request.session.get('current_person', None)
    if person is None:
        return redirect('index')
    else:
        at_this_address = Person.people.filter(street_address=" ".join(person.street_address.lower().split()))
        if len(at_this_address) > 0:
            return render(request, 'address_visited.html', {})
        else:
            request.session['current_person'] = person
            return redirect('status')


def status(request):
    person = request.session.get('current_person', None)
    if person is None:
        return redirect("index")
    else:
        if request.method == 'POST':
            form = forms.StatusQuestions(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                person.status = data['status']
                if person.status != "Not Home":
                    person.save()
                request.session['current_person'] = person
                if person.status != forms.WILLING_TO_PARTICIPATE:
                    print('redirect')
                    return redirect('success')
                return redirect('page_two')
        else:
            form = forms.StatusQuestions()
            return render(request, 'status.html', {
                'form': form
            })


def page_two(request):
    person = request.session.get('current_person', None)
    if person is None:
        return redirect("index")
    else:
        if request.method == 'POST':
            form = forms.ParticipantQuestions(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                person.ghc_rating = data['rate_ghc'] or -1
                person.ghc_impact = data['ghc_impact'] or -1
                person.ghc_involvement = data['ghc_involvement'] or ""
                person.target_involvement = data['desired_involvement'] or ""
                person.want_community_events = data['community_event_interest'] or ""
                person.religious_knowledge = data['religious_knowledge'] or ""
                person.religious_similarity = data['religious_similarity'] or ""
                person.religion = data['religious_identification'] or ""
                person.age_range = data['age_range'] or ""
                person.race = data['race_ethnicity'] or ""
                person.gender = data['gender'] or ""

                person.save()
                request.session['current_person'] = person
                return redirect('done')
        else:
            form = forms.ParticipantQuestions()
        return render(request, 'page_two.html', {
            'form': form,
    })


def done(request):
    person = request.session.get('current_person', None)
    if person is None:
        return redirect("index")
    else:
        return render(request, 'user_complete.html')


def page_three(request):
    person = request.session.get('current_person', None)
    if person is None:
        return redirect("index")
    else:
        if request.method == 'POST':
            form = forms.FollowUpQuestions(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                person.followup = data['follow_up'] or ""
                person.witnessed_to = data['witnessed_to'] or ""
                person.save()
                request.session['current_person'] = person
                if person.followup == "yes" and person.witnessed_to == "later":
                    return redirect('contact')
                else:
                    return redirect('notes')
        else:
            form = forms.FollowUpQuestions()
        return render(request, 'page_three.html', {
            'form': form,
        })


def contact(request):
    person = request.session.get('current_person', None)
    if person is None:
        return redirect("index")
    else:
        if request.method == 'POST':
            form = forms.ContactInfo(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                person.contact_info = data['contact_info'] or ""
                person.contact_type = data['contact_type'] or ""
                person.save()
                request.session['current_person'] = person
                return redirect('notes')

        else:
            form = forms.ContactInfo
        return render(request, 'contact_info.html', {
            'form': form,
        })


def notes(request):
    person = request.session.get('current_person', None)
    if person is None:
        return redirect("index")
    else:
        if request.method == 'POST':
            form = forms.Notes(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                person.notes = data['notes'] or ""
                person.save()
                request.session['current_person'] = person
                return redirect('success')
        else:
            form = forms.Notes
        return render(request, 'notes.html', {
            'form': form,
        })


def success(request):
    request.session.flush()
    return render(request, 'success.html')
