from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic

from .models import Paper, Note
from .forms import NoteForm

class PaperListView(generic.ListView):
	template_name = 'system/index.html'
	context_object_name = 'latest_paper_list'

	def get_queryset(self):
		"""Return the last five published questions."""
		return Paper.objects.order_by('-read_date')[:50]


class NoteListView(generic.ListView):
	template_name = 'system/note.html'
	context_object_name = 'latest_note_list'

	def get_queryset(self):
		"""Return the last five published questions."""
		return Note.objects.order_by('-add_date')[:50]


class NoteDetailView(generic.DetailView):
	template_name = "system/note.html"
	model = Note


class PaperDetailView(generic.DetailView):
	template_name = 'system/paper.html'
	model = Paper
	
def PaperCreateView(request, paper_id):
	paper = get_object_or_404(Paper, pk=paper_id)
	form = NoteForm()
	return render(request, 'system/paper_create.html', {'paper': paper, 'form': form})
	

def new_note(request, paper_id):

	try:
		paper = get_object_or_404(Paper, pk=paper_id)
		text = request.POST['text']
	except:
		# Redisplay the question voting form.
		return render(request, 'system:paper_detail', {
			'paper': paper,
			'error_message': "You didn't write anything",
		})
	else: 
		note = Note(paper=paper, text=text)	
		note.save()

		# Always return an HttpResponseRedirect after successfully dealing
		# with POST data. This prevents data from being posted twice if a
		# user hits the Back button.
		return HttpResponseRedirect(reverse('system:paper_detail', args=(paper.id,)))