# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse

from web.models import Posts, slider, Category


def navANDslider(request):
	categorys = Category.objects.all()
	slids = slider.objects.all()
	context = {
		'categorys' : categorys,
		'slider' : slids,
	}
	return context

def index(request):
	posts = Posts.objects.all()
	context = navANDslider(request)
	context['posts'] = posts
	return render(request,'index.html',context)

def page(request, title=''):
	 title = title.replace('-', ' ')
	 post = Posts.objects.filter(title = title)
	 context = navANDslider(request)
	 context['posts'] = post
	 return render(request,'page.html',context)

def category(request, cat_name = ''):
	cat_name = cat_name.replace('-', ' ')
	category_name = Category.objects.get(cat_name = cat_name)
	category_id = category_name.id
	posts = Posts.objects.filter(category = category_id)
	context = navANDslider(request)
	context['posts'] = posts
	return render (request,'category.html',context)
