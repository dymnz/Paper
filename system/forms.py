import datetime
from django.utils import timezone
from django import forms
from django.db import models

from markdownx.fields import MarkdownxFormField
from markdownx.widgets import MarkdownxWidget
from taggit.forms import TagField
from taggit.models import Tag

class NoteForm(forms.Form):
	#tags = TagField(widget=forms.TextInput(attrs={'class' : 'tag-field'}), max_length=200)

	tag_dropdown = forms.ChoiceField(choices=[(tag, tag) for tag in Tag.objects.all()], widget=forms.Select(attrs={'class':'tag-field'}), label='')
	text = MarkdownxFormField(widget=MarkdownxWidget(attrs={'class': 'text-box'}), label='', )
	


class PaperForm(forms.Form):
	title = forms.CharField(widget=forms.TextInput(attrs={'class' : 'text-field'}), max_length=200)
	author = forms.CharField(widget=forms.TextInput(attrs={'class' : 'text-field'}), max_length=200)
	intro = forms.CharField(widget=forms.TextInput(attrs={'class' : 'text-field'}), max_length=500)
	points = models.IntegerField()

	YEAR_CHOICES = []
	for r in range(1980, (datetime.datetime.now().year+1)):
		YEAR_CHOICES.append((r,r))

	publish_date = models.IntegerField(('year'), max_length=4, choices=YEAR_CHOICES, default=datetime.datetime.now().year)
	read_date = models.DateField('date read', default=timezone.now)
	





	
