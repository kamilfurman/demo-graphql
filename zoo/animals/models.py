# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name




class Food(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Spiece(models.Model):
    name = models.CharField(max_length=20) 
    foods = models.ManyToManyField(Food, related_name='spieces', null=True)
    countries = models.ManyToManyField(Country, related_name='spieces', null=True)

    def __str__(self):
        return self.name


class Animal(models.Model):
    name = models.CharField(max_length=20)
    spiece = models.ForeignKey(Spiece)

    def __str__(self):
        return self.name

class Zoo(models.Model):
    name = models.CharField(max_length=20)
    country = models.ForeignKey(Country, related_name='zoos')
    animals = models.ManyToManyField(Animal, related_name='zoos', null=True)
    def __str__(self):
        return self.name