# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse

from .models import Posts,slider

def index(request):
	posts = Posts.objects.all();
	slids = slider.objects.all();
	context = {
		'posts' : posts,
		'slider' : slids,
	}
	return render(request,'index.html',context)

def page(request, title=''):
	 title = title.replace('-', ' ')
	 post = Posts.objects.filter(title = title)
	 context = {
	 	'posts' : post,
	 }
	 return render(request,'page.html',context)
