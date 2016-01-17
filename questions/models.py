from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=25, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    zip = models.IntegerField()
    status = models.CharField(max_length=100)
    religion = models.CharField(max_length=50, null=True, blank=True)
    ghc_helpfulness = models.IntegerField(null=True, blank=True)
