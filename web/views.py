# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Posts,slider

def index(request):
	posts = Posts.objects.all();
	slids = slider.objects.all();
	context = {
		'posts' : posts,
		'slider' : slids,
	}
	return render(request,'index.html',context)
