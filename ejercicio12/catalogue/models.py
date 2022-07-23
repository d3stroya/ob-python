from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=12, help_text="Write the film genre (thriller, comedy, drama,...).")

    def __str__(self):
        return self.name

class Casting(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def __str__(self):
        return "%s (%s)" % (self.last_name, self.first_name)

class Awards(models.Model):
    award = models.CharField(max_length=40, null=True, blank=True, help_text="Which award did this film win?")

    def __str__(self):
        return self.award

class Film(models.Model):
    title = models.CharField(max_length=32)
    genre = models.ManyToManyField(Genre)
    year = models.IntegerField(null=True)
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=300, help_text="Make a short description of the argument of the film.")
    casting = models.ManyToManyField(Casting)
    awards = models.ManyToManyField(Awards)

    def __str__(self):
        return self.title

class Director(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


