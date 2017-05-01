from django.conf.urls import url

from . import views

app_name = 'system'
urlpatterns = [
	url(r'^$', views.PaperListView.as_view(), name='paper_list'),
    url(r'^note/$', views.NoteListView.as_view(), name='note_list'),
    url(r'^note/(?P<pk>[0-9]+)/$', views.NoteDetailView.as_view(), name='note_detail'),
    #url(r'^(?P<pk>[0-9]+)/$', views.PaperDetailView.as_view(), name='paper_detail'),
    url(r'^(?P<paper_id>[0-9]+)/$', views.PaperCreateView, name='paper_detail'),
    url(r'^(?P<paper_id>[0-9]+)/new_note/$', views.new_note, name='new_note'),
]
