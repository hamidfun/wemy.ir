# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
#add users
from django.contrib.auth.models import User
#ckeditor
from ckeditor_uploader.fields import RichTextUploadingField
#translattion
from django.utils.translation import ugettext_lazy as _
class Posts(models.Model):
	title = models.CharField(max_length=255)
	content = RichTextUploadingField()
	excerpt = models.TextField(help_text =  'پیش فرض مقداری از متن اصلی گرفته میشود', blank = True, null = True)
	author = models.ForeignKey(User, null=True, blank=False, default = User)
	status = models.CharField(max_length=20, default = 'publish')
	comment_status = models.CharField(max_length = 20, default = 'open')
	password = models.CharField(max_length=20,blank = True, null = True )
	img = models.ImageField(_('main image'), upload_to='posts/%Y/%m/%d', blank=True, null=True)
	url = models.CharField(max_length = 200, help_text = '(پیش فرض اسلش عنوان مطلب)', blank = True, null = True )
	date = models.DateTimeField(auto_now=True,auto_now_add=False)
	date_modify = models.DateTimeField(auto_now = False, auto_now_add=True)

	def __unicode__(self):
		return self.title

class slider(models.Model):
	author = models.ForeignKey(User)
	date = models.DateTimeField()
	img = models.TextField()
	title = models.TextField()
class Opt(models.Model):
	key = models.CharField(max_length = 255)
	value = RichTextUploadingField()
	def __unicode__(self):
		return "{} - {}".format(self.key,self.value)
