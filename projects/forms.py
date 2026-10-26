from django import forms
from .models import MusicProject, Task, Note, TrackVersion


class MusicProjectForm(forms.ModelForm):
    class Meta:
        model = MusicProject
        fields = [
            'title',
            'description',
            'genre',
            'status',
            'bpm',
            'musical_key',
            'release_date',
            'duration',
            'cover',
        ]

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'status',
            'due_date',
        ]

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']

class TrackVersionForm(forms.ModelForm):
    class Meta:
        model = TrackVersion
        fields = ['name', 'description']