from django import forms

STATUS_OPTIONS = (("Willing to Participate", 'Willing to Participate'),
                  ("Not Willing to Participate", 'Not Willing to Participate'),
                  ('Not Home', 'Not Home'))

RATE_1_TO_5 = ((1,1),
               (2,2),
               (3,3),
               (4,4),
               (5,5))

INVOLVEMENT = (("not involved","not involved"),
               ("not very involved","not very involved"),
               ("somewhat involved","somewhat involved"),
               ("involved","involved"),
               ("very involved","very involved"))

YES_NO = (("yes","yes"),
          ("no","no"))

NOW_LATER = (("now", "now"),
             ("later", "later"))

SIMILARITY = (("very different", "very different"),
              ("different", "different"),
              ("unsure","unsure"),
              ("similar", "similar"),
              ("very similar", "very similar"))

RELIGIONS = (("Agnosticism","Agnosticism"),
             ("Atheism","Atheism"),
             ("Buddhism", "Buddhism"),
             ("Christianity", "Christianity"),
             ("Hinduism", "Hinduism"),
             ("Islam", "Islam"),
             ("Judaism", "Judaism"),
             ("Shintoism", "Shintoism"),
             ("Taoism", "Taoism"),
             ("Other", "Other"))

AGES = (("under 18", "under 18"),
        ("18-30", "18-30"),
        ("31-50", "31-50"),
        ("51-70", "51-70"),
        ("over 70", "over 70"),
        ("prefer to not disclose", "prefer to not disclose"))

RACES = (("American Indian/Alaskan Native", "American Indian/Alaskan Native"),
         ("Asian", "Asian"),
         ("Black/African American", "Black/African American"),
         ("Native Hawaiian/Other Pacific Islander", "Native Hawaiian/Other Pacific Islander"),
         ("White", "White"),
         ("prefer to not disclose", "prefer to not disclose"))

GENDER = (("Male", "Male"),
          ("Female", "Female"),
          ("prefer to not disclose", "prefer to not disclose"))


class PrelimQuestions(forms.Form):
    street_address = forms.CharField(max_length=100)
    city = forms.CharField(max_length=50)
    zip = forms.IntegerField()
    status = forms.ChoiceField(widget=forms.Select, choices=STATUS_OPTIONS)


class ParticipantQuestions(forms.Form):

    rate_ghc = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=RATE_1_TO_5,
        label="How would you rate your interactions with GHC thus far?",
        required=False
    )

    ghc_impact = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=RATE_1_TO_5,
        label="How positive is GHC's impact on the neighborhood?",
        required=False
    )

    ghc_involvement = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=INVOLVEMENT,
        label="How involved do you feel GHC is in your neighborhood?",
        required=False
    )

    desired_involvement = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=INVOLVEMENT,
        label="How involved would you like GHC to be in your neighborhood?",
        required=False
    )

    community_event_interest = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=YES_NO,
        label="Would you be interested in attending community events held at GHC?",
        required=False
    )

    religious_similarity = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=SIMILARITY,
        label="How would you say GHC's religious beliefs compare to yours?",
        required=False
    )

    religious_identification = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=RELIGIONS,
        label="Do you identify with a major world religion?",
        required=False
    )

    age_range = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=AGES,
        label="What is your age range",
        required=False
    )

    race_ethnicity = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=RACES,
        label="What is your race/ethnicity?",
        required=False
    )

    gender = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=GENDER,
        label="What is your gender?",
        required=False
    )


class FollowUpQuestions(forms.Form):

    follow_up = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=YES_NO,
        label="Would you be interested in learning more about what we believe at Green Hills",
        required=False
    )

    witnessed_to = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=NOW_LATER,
        label="If yes, do you have time now, or should we contact you later?",
        required=False
    )

    contact_info = forms.CharField(max_length=50, required=False)
