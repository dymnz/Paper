import datetime

from django.db import models
from django.utils import timezone

from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from taggit.managers import TaggableManager

class Paper(models.Model):
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=200)
	intro = models.CharField(max_length=500)


	YEAR_CHOICES = []
	for r in range(1980, (datetime.datetime.now().year+1)):
		YEAR_CHOICES.append((r,r))

	publish_date = models.IntegerField(('year'), max_length=4, choices=YEAR_CHOICES, default=datetime.datetime.now().year)
	#publish_date = models.DateField('date published', default=timezone.now)

	read_date = models.DateField('date read', default=timezone.now)
	points = models.IntegerField(default=0)

	tags = TaggableManager(blank=True)

	def __str__(self):
		return self.title

	def read_recently(self):
		return self.read_date >= timezone.now() - datetime.timedelta(days=7)
		
	def formatted_markdown(self):
		return markdownify(self.text)		

class Note(models.Model):
	paper = models.ForeignKey(Paper, on_delete=models.CASCADE)
	add_date = models.DateField('date added', default=timezone.now)

	text = MarkdownxField()
	tags = TaggableManager(blank=True)

	def __str__(self):
		return self.text
		
	def formatted_markdown(self):
		return markdownify(self.text)

	