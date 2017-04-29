from django.shortcuts import get_object_or_404, render
from django.http import Http404

from .models import Paper

def index(request):
	latest_paper_list = Paper.objects.order_by('-read_date')[:50]
	context = {
		'latest_paper_list': latest_paper_list,
	}
	return render(request, 'system/index.html', context)

def paper(request, paper_id):
	paper = get_object_or_404(Paper, pk=paper_id)
	return render(request, 'system/paper.html', {'paper': paper})

def note(request, paper_id):
	response = "You're looking at the notes of paper %s."
	return HttpResponse(response % paper_id)


