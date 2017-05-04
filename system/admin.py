from django.contrib import admin

from .models import Paper, Note, Text


class NoteInline(admin.StackedInline):
    model = Note
    extra = 1
    fields = ['text', 'tags']


class TextInline(admin.StackedInline):
    model = Text
    extra = 1
    fields = ['text']

class PaperAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'publish_date']}),
        ('Custom', {'fields': ['read_date']}),
    ]
    inlines = [TextInline, NoteInline]


admin.site.register(Paper, PaperAdmin)