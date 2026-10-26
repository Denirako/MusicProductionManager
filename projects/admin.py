from django.contrib import admin
from .models import Genre, MusicProject, Task, Note, TrackVersion


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(MusicProject)
class MusicProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'status', 'bpm', 'release_date')
    list_filter = ('status', 'genre')
    search_fields = ('title', 'description', 'musical_key')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'status', 'due_date')
    list_filter = ('status', 'project')
    search_fields = ('title', 'description')

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'created_at', 'updated_at')
    list_filter = ('project',)
    search_fields = ('title', 'content')

@admin.register(TrackVersion)
class TrackVersionAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', 'created_at')
    list_filter = ('project',)
    search_fields = ('name', 'description')