from django import forms
from .models import MusicProject, Task, Note, TrackVersion

from django.utils.translation import gettext_lazy as _


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

        labels = {
            'title': _('Title'),
            'description': _('Description'),
            'genre': _('Genre'),
            'status': _('Status'),
            'bpm': _('BPM'),
            'musical_key': _('Musical key'),
            'release_date': _('Release date'),
            'duration': _('Duration'),
            'cover': _('Cover'),
        }

        help_texts = {
            'duration': _('Duration in seconds'),
        }

        widgets = {
            'bpm': forms.NumberInput(attrs={
                'min': 1,
                'max': 300,
                'placeholder': 'e.g. 128',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['genre'].empty_label = _('Select an option')

        key_choices = list(self.fields['musical_key'].choices)
        key_choices[0] = ('', _('Select an option'))
        self.fields['musical_key'].choices = key_choices

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'status',
            'due_date',
        ]

        labels = {
            'title': _('Title'),
            'description': _('Description'),
            'status': _('Status'),
            'due_date': _('Due date'),
        }

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']
        labels = {
            'title': _('Title'),
            'content': _('Content'),
        }

class TrackVersionForm(forms.ModelForm):
    class Meta:
        model = TrackVersion
        fields = ['name', 'description']

        labels = {
            'name': _('Name'),
            'description': _('Description'),
        }

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Enter version name'),
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': _('Describe this version'),
            }),
        }