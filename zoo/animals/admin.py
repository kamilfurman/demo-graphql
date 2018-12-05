# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from .models import Animal, Country, Spiece, Zoo, Food


admin.site.register(Animal)
admin.site.register(Country)
admin.site.register(Spiece)
admin.site.register(Zoo)
admin.site.register(Food)
