from django.conf.urls import url  # include,
# from django.contrib import admin
from .views import index_view, add_note, add_tag, show_tag
app_name = 'notes'


urlpatterns = [
    url(r'^$', index_view, name='index'),
    url(r'^addnote/', add_note, name='addnote'),
    url(r'^addtag/', add_tag, name='addtag'),
    url(r'^showtag/(?P<tagid>[-\w]+)/$', show_tag, name='showtag')
]
