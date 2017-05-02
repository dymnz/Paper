from django.conf.urls import url

from . import views

app_name = 'system'
urlpatterns = [
	url(r'^$', views.PaperListView, name='paper_list'),
    url(r'^note/$', views.NoteListView.as_view(), name='note_list'),
    url(r'^new_paper/$', views.PaperListCreateView, name='new_paper'),
    url(r'^note/(?P<pk>[0-9]+)/$', views.NoteDetailView.as_view(), name='note_detail'),
    url(r'^(?P<paper_id>[0-9]+)/$', views.PaperDetailView, name='paper_detail'),
]
