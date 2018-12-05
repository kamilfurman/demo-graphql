
from .models import Animal, Country, Spiece, Zoo, Food
from graphene_django import DjangoObjectType
import graphene


class AnimalType(DjangoObjectType):
    class Meta:
        model = Animal



class Query(object):
    animals = graphene.List(AnimalType)

    def resolve_animals(self, info, **kwargs):
        return Animal.objects.all()
