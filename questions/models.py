from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=50)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    zip = models.IntegerField()
    religion = models.CharField(max_length=50)
    ghc_helpfulness = models.IntegerField()
