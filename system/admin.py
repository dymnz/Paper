from django.contrib import admin

from .models import Paper, Note


class NoteInline(admin.StackedInline):
    model = Note
    extra = 1
    fields = ['text']

class PaperAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'publish_date']}),
        ('Custom', {'fields': ['read_date', 'text']}),
    ]
    inlines = [NoteInline]


admin.site.register(Paper, PaperAdmin)