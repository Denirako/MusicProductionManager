from django.shortcuts import render, redirect, get_object_or_404
from .forms import MusicProjectForm, TaskForm, NoteForm, TrackVersionForm
from .models import MusicProject, Task, Note, Genre, TrackVersion
from django.core.paginator import Paginator


def home(request):
    return render(request, 'projects/home.html')

def project_list(request):
    search_query = request.GET.get('search', '')
    genre_id = request.GET.get('genre', '')
    status = request.GET.get('status', '')

    projects = MusicProject.objects.filter(
        title__icontains=search_query
    )

    if genre_id:
        projects = projects.filter(genre_id=genre_id)

    if status:
        projects = projects.filter(status=status)

    genres = Genre.objects.all()

    projects = projects.order_by('id')

    paginator = Paginator(projects, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    statuses = MusicProject.STATUS_CHOICES

    return render(
        request,
        'projects/project_list.html',
        {
            'projects': page_obj,
            'page_obj': page_obj,
            'genres': genres,
            'statuses': statuses
        }
    )

def project_detail(request, pk):
    project = get_object_or_404(MusicProject, pk=pk)
    tasks = project.tasks.all()
    notes = Note.objects.filter(project=project)
    versions = project.versions.all()

    print([(note.id, note.title) for note in notes])

    return render(
        request,
        'projects/project_detail.html',
        {
            'project': project,
            'tasks': tasks,
            'notes': notes,
            'versions': versions,
        }
    )

def task_create(request, pk):
    project = get_object_or_404(MusicProject, pk=pk)

    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = TaskForm()

    return render(
        request,
        'projects/task_form.html',
        {
            'form': form,
            'project': project
        }
    )

def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    project = task.project

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = TaskForm(instance=task)

    return render(
        request,
        'projects/task_form.html',
        {
            'form': form,
            'project': project
        }
    )

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    project = task.project

    if request.method == 'POST':
        task.delete()
        return redirect('project_detail', pk=project.pk)

    return render(
        request,
        'projects/task_delete.html',
        {
            'task': task,
            'project': project
        }
    )

def note_create(request, pk):
    project = get_object_or_404(MusicProject, pk=pk)

    if request.method == 'POST':
        form = NoteForm(request.POST)

        if form.is_valid():
            note = form.save(commit=False)
            note.project = project
            note.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = NoteForm()

    return render(
        request,
        'projects/note_form.html',
        {
            'form': form,
            'project': project
        }
    )

def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk)
    project = note.project

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)

        if form.is_valid():
            form.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = NoteForm(instance=note)

    return render(
        request,
        'projects/note_form.html',
        {
            'form': form,
            'project': project
        }
    )

def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    project = note.project

    if request.method == 'POST':
        note.delete()
        return redirect('project_detail', pk=project.pk)

    return render(
        request,
        'projects/note_delete.html',
        {
            'note': note,
            'project': project
        }
    )

def project_create(request):
    form = MusicProjectForm()

    if request.method == 'POST':
        form = MusicProjectForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('project_list')

    return render(request, 'projects/project_form.html', {'form': form})

def project_edit(request, pk):
    project = get_object_or_404(MusicProject, pk=pk)

    if request.method == 'POST':
        form = MusicProjectForm(request.POST, request.FILES, instance=project)

        if form.is_valid():
            form.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = MusicProjectForm(instance=project)

    return render(request, 'projects/project_form.html', {'form': form})

def project_delete(request, pk):
    project = get_object_or_404(MusicProject, pk=pk)

    if request.method == 'POST':
        project.delete()
        return redirect('project_list')

    return render(request, 'projects/project_delete.html', {'project': project})

def track_version_create(request, pk):
    project = get_object_or_404(MusicProject, pk=pk)

    if request.method == 'POST':
        form = TrackVersionForm(request.POST)

        if form.is_valid():
            version = form.save(commit=False)
            version.project = project
            version.save()

            return redirect('project_detail', pk=project.pk)
    else:
        form = TrackVersionForm()

    return render(
        request,
        'projects/track_version_form.html',
        {
            'form': form,
            'project': project
        }
    )

def track_version_edit(request, pk):
    version = get_object_or_404(TrackVersion, pk=pk)
    project = version.project

    if request.method == 'POST':
        form = TrackVersionForm(request.POST, instance=version)

        if form.is_valid():
            form.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = TrackVersionForm(instance=version)

    return render(
        request,
        'projects/track_version_form.html',
        {
            'form': form,
            'project': project,
            'version': version,
        }
    )


def track_version_delete(request, pk):
    version = get_object_or_404(TrackVersion, pk=pk)
    project = version.project

    if request.method == 'POST':
        version.delete()
        return redirect('project_detail', pk=project.pk)

    return render(
        request,
        'projects/track_version_confirm_delete.html',
        {
            'version': version,
            'project': project,
        }
    )

