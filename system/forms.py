from django import forms

from markdownx.fields import MarkdownxFormField
from markdownx.widgets import MarkdownxWidget


class NoteForm(forms.Form):
    text = MarkdownxFormField()