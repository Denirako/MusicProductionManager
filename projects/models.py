from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from django.utils.translation import gettext_lazy as _

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class MusicProject(models.Model):

    STATUS_CHOICES = [
        ('IDEA', _('Idea')),
        ('IN_PROGRESS', _('In Progress')),
        ('MIXING', _('Mixing')),
        ('MASTERING', _('Mastering')),
        ('RELEASED', _('Released')),
    ]

    MUSICAL_KEY_CHOICES = [
        ('C major', 'C major'),
        ('C minor', 'C minor'),
        ('C# major', 'C# major'),
        ('C# minor', 'C# minor'),
        ('D major', 'D major'),
        ('D minor', 'D minor'),
        ('D# major', 'D# major'),
        ('D# minor', 'D# minor'),
        ('E major', 'E major'),
        ('E minor', 'E minor'),
        ('F major', 'F major'),
        ('F minor', 'F minor'),
        ('F# major', 'F# major'),
        ('F# minor', 'F# minor'),
        ('G major', 'G major'),
        ('G minor', 'G minor'),
        ('G# major', 'G# major'),
        ('G# minor', 'G# minor'),
        ('A major', 'A major'),
        ('A minor', 'A minor'),
        ('A# major', 'A# major'),
        ('A# minor', 'A# minor'),
        ('B major', 'B major'),
        ('B minor', 'B minor'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    genre = models.ForeignKey(
        Genre,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='IDEA'
    )

    bpm = models.IntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(300)
        ]
    )

    musical_key = models.CharField(
        max_length=20,
        choices=MUSICAL_KEY_CHOICES,
        blank=True
    )

    release_date = models.DateField(
        null=True,
        blank=True
    )

    duration = models.PositiveIntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(1)],
        help_text='Duration in seconds'
    )

    cover = models.ImageField(
        upload_to='project_covers/',
        blank=True,
        null=True
    )

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Task(models.Model):
    project = models.ForeignKey(
        MusicProject,
        on_delete=models.CASCADE,
        related_name='tasks'
    )

    title = models.CharField(max_length=200)

    description = models.TextField(blank=True)

    STATUS_CHOICES = [
        ('TODO', _('To Do')),
        ('IN_PROGRESS', _('In Progress')),
        ('DONE', _('Done')),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='TODO'
    )

    due_date = models.DateField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title

class Note(models.Model):
    project = models.ForeignKey(
        MusicProject,
        on_delete=models.CASCADE,
        related_name='notes'
    )

    title = models.CharField(max_length=200)

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class TrackVersion(models.Model):
    project = models.ForeignKey(
        MusicProject,
        on_delete=models.CASCADE,
        related_name='versions'
    )

    name = models.CharField(max_length=200)

    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name