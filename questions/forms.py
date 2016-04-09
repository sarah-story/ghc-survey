from django import forms

WILLING_TO_PARTICIPATE = "Willing to Participate"

STATUS_OPTIONS = ((WILLING_TO_PARTICIPATE, WILLING_TO_PARTICIPATE),
                  ("Not Willing to Participate", 'Not Willing to Participate'),
                  ('Not Home', 'Not Home'))

RATE_1_TO_5 = ((-1, "None Selected"),
               (1,1),
               (2,2),
               (3,3),
               (4,4),
               (5,5))

INVOLVEMENT = (("", "None Selected"),
               ("not involved","not involved"),
               ("not very involved","not very involved"),
               ("somewhat involved","somewhat involved"),
               ("involved","involved"),
               ("very involved","very involved"))

YES_NO = (("", "None Selected"),
          ("yes","yes"),
          ("no","no"))

NOW_LATER = (("", "None Selected"),
             ("now", "now"),
             ("later", "later"))

SIMILARITY = (("", "None Selected"),
              ("very different", "very different"),
              ("different", "different"),
              ("unsure","unsure"),
              ("similar", "similar"),
              ("very similar", "very similar"))

RELIGIONS = (("", "None Selected"),
             ("Agnosticism","Agnosticism"),
             ("Atheism","Atheism"),
             ("Buddhism", "Buddhism"),
             ("Christianity", "Christianity"),
             ("Hinduism", "Hinduism"),
             ("Islam", "Islam"),
             ("Judaism", "Judaism"),
             ("Shintoism", "Shintoism"),
             ("Taoism", "Taoism"),
             ("Other", "Other"))

AGES = (("", "None Selected"),
        ("under 18", "under 18"),
        ("18-30", "18-30"),
        ("31-50", "31-50"),
        ("51-70", "51-70"),
        ("over 70", "over 70"),
        ("prefer to not disclose", "prefer to not disclose"))

RACES = (("", "None Selected"),
         ("American Indian/Alaskan Native", "American Indian/Alaskan Native"),
         ("Asian", "Asian"),
         ("Black/African American", "Black/African American"),
         ("Native Hawaiian/Other Pacific Islander", "Native Hawaiian/Other Pacific Islander"),
         ("White", "White"),
         ("prefer to not disclose", "prefer to not disclose"))

GENDER = (("", "None Selected"),
          ("Male", "Male"),
          ("Female", "Female"),
          ("prefer to not disclose", "prefer to not disclose"))

CONTACT_TYPE = (("", "None Selected"),
                ("email", "Email"),
                ("phone", "Phone"))


class PrelimQuestions(forms.Form):
    street_address = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control', 'placeholder': 'e.g. 101 Bowling'
    }), max_length=100, label="Street Address (don't include Drive, Ave, etc.):")


class StatusQuestions(forms.Form):
    status = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=STATUS_OPTIONS,
        label="The resident is:"
    )


class ParticipantQuestions(forms.Form):

    rate_ghc = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=RATE_1_TO_5,
        label="How would you rate your interactions with GHC thus far?",
        required=False
    )

    ghc_impact = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=RATE_1_TO_5,
        label="How positive is GHC's impact on the neighborhood?",
        required=False
    )

    ghc_involvement = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=INVOLVEMENT,
        label="How involved do you feel GHC is in your neighborhood?",
        required=False
    )

    desired_involvement = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=INVOLVEMENT,
        label="How involved would you like GHC to be in your neighborhood?",
        required=False
    )

    community_event_interest = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=YES_NO,
        label="Would you be interested in attending community events held at GHC?",
        required=False
    )

    religious_similarity = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=SIMILARITY,
        label="How would you say GHC's religious beliefs compare to yours?",
        required=False
    )

    religious_identification = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=RELIGIONS,
        label="Do you identify with a major world religion?",
        required=False
    )

    age_range = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=AGES,
        label="What is your age range",
        required=False
    )

    race_ethnicity = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=RACES,
        label="What is your race/ethnicity?",
        required=False
    )

    gender = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=GENDER,
        label="What is your gender?",
        required=False
    )


class FollowUpQuestions(forms.Form):

    follow_up = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=YES_NO,
        label="Would you be interested in learning more about what we believe at Green Hills",
        required=False
    )

    witnessed_to = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=NOW_LATER,
        label="If yes, do you have time now, or should we contact you later?",
        required=False
    )

class ContactInfo(forms.Form):

    contact_type = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=CONTACT_TYPE,
        label="What's the best way to contact you?",
        required=False
    )

    contact_info = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=50,
        required=False
    )
