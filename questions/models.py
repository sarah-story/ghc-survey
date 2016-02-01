from django.db import models


class Person(models.Model):
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    zip = models.IntegerField()
    status = models.CharField(max_length=100)

    ghc_rating = models.IntegerField(null=True, blank=True)
    ghc_impact = models.IntegerField(null=True, blank=True)
    ghc_involvement = models.CharField(max_length=25, null=True, blank=True)
    target_involvement = models.CharField(max_length=25, null=True, blank=True)
    want_community_events = models.CharField(max_length=3, null=True, blank=True)
    religious_knowledge = models.CharField(max_length=3, null=True, blank=True)
    religious_similarity = models.CharField(max_length=25, null=True, blank=True)
    religion = models.CharField(max_length=25, null=True, blank=True)
    age_range = models.CharField(max_length=25, null=True, blank=True)
    race = models.CharField(max_length=40, null=True, blank=True)
    gender = models.CharField(max_length=25, null=True, blank=True)

    followup = models.CharField(max_length=3, null=True, blank=True)
    witnessed_to = models.CharField(max_length=10, null=True, blank=True)
    contact_type = models.CharField(max_length=50, null=True, blank=True)
    contact_info = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.street_address
