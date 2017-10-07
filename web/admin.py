# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import Posts, Category, Slider, Opt

admin.site.register(Posts)
admin.site.register(Category)
admin.site.register(Slider)
admin.site.register(Opt)
