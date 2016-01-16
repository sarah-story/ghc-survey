from django import forms

STATUS_OPTIONS = ((1, 'Willing to Participate'), (2, 'Not Willing to Participate'), (3, 'Not Home'))


class PrelimQuestions(forms.Form):
    street_address = forms.CharField(max_length=100)
    city = forms.CharField(max_length=50)
    zip = forms.IntegerField()
    status = forms.ChoiceField(widget=forms.Select, choices=STATUS_OPTIONS)
