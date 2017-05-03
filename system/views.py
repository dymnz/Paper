from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic

from .models import Paper, Note
from .forms import NoteForm, PaperForm


def PaperListView(request):
	latest_paper_list = Paper.objects.order_by('-read_date')[:5]
	context = {'latest_paper_list': latest_paper_list}
	return render(request, 'system/index.html', context)

def _PaperListCreateView(request):
	latest_paper_list = Paper.objects.order_by('-read_date')[:5]
	context = {'latest_paper_list': latest_paper_list, 'form': PaperForm()}
	return render(request, 'system/index_create.html', context)


class NoteListView(generic.ListView):
	template_name = 'system/note.html'
	context_object_name = 'latest_note_list'

	# Collect every tag
	tag_list = []	
	for note in Note.objects.all():
		for tag in note.tags.names():
			tag_list.append(tag)
	tag_list = sorted(list(set(tag_list)))
		
	# Reorder the notes
	remaining_note_list = Note.objects.all()
	ordered_note_list = []
	for tag in tag_list:
		if len(remaining_note_list) == 0:
			break
		tag_note_list = list(remaining_note_list.filter(tags__name__in=[tag]))
		ordered_note_list.append(tag_note_list)
		# TODO: Remove assigned notes from remaining list #
		#remaining_note_list = remaining_note_list - tag_note_list




	def get_queryset(self):
		"""Return the last five published questions."""
		#return Note.objects.order_by('-add_date')[:50]
		return self.ordered_note_list


class NoteDetailView(generic.DetailView):
	template_name = "system/note.html"
	model = Note

	
def PaperCreateView(request, paper_id):
	paper = get_object_or_404(Paper, pk=paper_id)
	form = NoteForm()
	return render(request, 'system/paper_detail.html', {'paper': paper, 'form': form})
	

def PaperDetailView(request, paper_id):
	paper = get_object_or_404(Paper, pk=paper_id)
	if request.method == 'POST':
		
		# create a form instance and populate it with data from the request:
		form = NoteForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			note = Note(paper=paper, text=form.cleaned_data['text'])
			note.save()
			
			note.tags.add(form.cleaned_data['tag_dropdown'])

			# Reorganize the tags of a note
			for note in paper.note_set.all():
				sorted_tags = sorted(note.tags.names())
				note.tags.clear()
				for tag in sorted_tags:
					note.tags.add(tag)

			return HttpResponseRedirect(reverse('system:paper_detail', args=(paper.id,)))

	# if a GET (or any other method) we'll create a blank form
	else:
		form = NoteForm()

		# Collect every tag
		tag_list = []	
		for note in paper.note_set.all():
			for tag in note.tags.names():
				tag_list.append(tag)
		tag_list = sorted(list(set(tag_list)))
			
		# Reorder the notes
		remaining_note_list = paper.note_set.all()
		ordered_note_list = []
		for tag in tag_list:
			if len(remaining_note_list) == 0:
				break
			tag_note_list = list(remaining_note_list.filter(tags__name__in=[tag]))
			ordered_note_list.append(tag_note_list)
			# TODO: Remove assigned notes from remaining list #
			#remaining_note_list = remaining_note_list - tag_note_list
			
	return render(request, 'system/paper_detail.html', {'paper': paper, 'ordered_note_list': ordered_note_list, 'form': form})



def PaperListCreateView(request):

	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = PaperForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			# process the data in form.cleaned_data as required
			# ...
			# redirect to a new URL:
			return HttpResponseRedirect(reverse('system:paper_detail', args=(paper.id,)))

	# if a GET (or any other method) we'll create a blank form
	else:
		latest_paper_list = Paper.objects.order_by('-read_date')[:5]
		context = {'latest_paper_list': latest_paper_list, 'form': PaperForm()}
	return render(request, 'system/new_paper.html', context)