import datetime

from django.db import models
from django.utils import timezone

from markdownx.models import MarkdownxField
from taggit.managers import TaggableManager

class Paper(models.Model):
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=200)
	intro = models.CharField(max_length=500)
	publish_date = models.DateField('date published', default=timezone.now)
	read_date = models.DateField('date read', default=timezone.now)
	points = models.IntegerField(default=0)

	text = MarkdownxField()
	tags = TaggableManager()

	def __str__(self):
		return self.title

	def read_recently(self):
		return self.read_date >= timezone.now() - datetime.timedelta(days=7)

class Note(models.Model):
	paper = models.ForeignKey(Paper, on_delete=models.CASCADE)
	add_date = models.DateField('date published', default=timezone.now)

	text = MarkdownxField()
	tags = TaggableManager()

	def __str__(self):
		return self.text

    