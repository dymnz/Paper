from django.conf.urls import url

from . import views

app_name = 'paper'
urlpatterns = [
	# ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /paper/5/
    url(r'^(?P<paper_id>[0-9]+)/$', views.paper, name='paper'),
    # ex: /paper/5/notes/
    url(r'^(?P<paper_id>[0-9]+)/note/$', views.note, name='note'),
    url(r'^(?P<paper_id>[0-9]+)/new_note/$', views.new_note, name='new_note'),
]
