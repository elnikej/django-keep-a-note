from django.shortcuts import render, get_object_or_404  # render_to_response,
# from django.template import RequestContext, loader
from django.http import HttpResponseRedirect  # HttpResponse,
from django.contrib import messages
from django.urls import reverse
from .models import Notes, Tag
from .forms import NoteForm, TagForm

from django.contrib.auth.decorators import user_passes_test


def user_only(user):
    return user.is_authenticated


@user_passes_test(user_only, login_url="/")
def index_view(request):
    notes = Notes.objects.all().filter(owner=request.user)
    tags = Tag.objects.all()
    return render(request, 'notesIndex.html', {'notes': notes, 'tags': tags})


@user_passes_test(user_only, login_url="/")
def add_note(request):
    id = request.GET.get('id', None)
    if id is not None:
        note = get_object_or_404(Notes, id=id)
    else:
        note = None
    if request.method == 'POST':
        if request.POST.get('control') == 'delete':
            note.delete()
            messages.add_message(request, messages.INFO, 'Note Deleted!')
            return HttpResponseRedirect(reverse('notes:index'))
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner = request.user
            obj.save()
            messages.add_message(request, messages.INFO, 'Note Added!')
            return HttpResponseRedirect(reverse('notes:index'))
    else:
        form = NoteForm(instance=note)
    return render(request, 'addNote.html', {'form': form, 'note': note})


@user_passes_test(user_only, login_url="/")
def add_tag(request):
    id = request.GET.get('id', None)
    if id is not None:
        tag = get_object_or_404(Tag, id=id)
    else:
        tag = None
    if request.method == 'POST':
        if request.POST.get('control') == 'delete':
            tag.delete()
            messages.add_message(request, messages.INFO, 'Tag Deleted!')
            return HttpResponseRedirect(reverse('notes:index'))
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Tag Added!')
            return HttpResponseRedirect(reverse('notes:index'))
    else:
        form = TagForm(instance=tag)
    return render(request, 'addTag.html', {'form': form, 'tag': tag})


@user_passes_test(user_only, login_url="/")
def show_tag(request, tagid=None):
    """show only Note with tagid"""
    # taglist = Tag.objects.filter(pk=tagid)
    # notes = Notes.objects.filter(tags__in=taglist).filter(owner=request.user)
    notes = Notes.objects.filter(tags_id=tagid).filter(owner=request.user)
    tags = Tag.objects.all()
    return render(request, 'notesIndex.html', {'notes': notes, 'tags': tags})
