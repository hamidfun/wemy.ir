# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
#add users
from django.contrib.auth.models import User

#ckeditor
from ckeditor_uploader.fields import RichTextUploadingField

class Posts(models.Model):
	author = models.ForeignKey(User)
	date = models.DateTimeField(auto_now=True,auto_now_add=False)
	date_md = models.DateTimeField(auto_now = False, auto_now_add=True)
	content = RichTextUploadingField()
	title = models.CharField(max_length=255)
	excerpt = models.TextField()
	status = models.CharField(max_length=20, default = 'publish')
	comment_status = models.CharField(max_length = 20, default = 'open')
	password = models.CharField(max_length=20)
	img = models.CharField(max_length = 255)
	
