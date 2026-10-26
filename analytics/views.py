from django.shortcuts import render
from projects.models import MusicProject, Task
from django.db.models import Count

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import pandas as pd
import io
import base64


def dashboard(request):
    total_projects = MusicProject.objects.count()

    project_data = MusicProject.objects.values(
        'title',
        'genre__name',
        'status',
        'bpm',
    )

    df = pd.DataFrame(list(project_data))

    if not df.empty:
        genre_analysis = (
            df['genre__name']
            .fillna('No Genre')
            .value_counts()
        )
    else:
        genre_analysis = pd.Series(dtype='int64')

    genre_stats = (
        MusicProject.objects
        .values('genre__name')
        .annotate(total=Count('id'))
        .order_by('-total')
    )

    idea_projects = MusicProject.objects.filter(status='IDEA').count()
    in_progress_projects = MusicProject.objects.filter(status='IN_PROGRESS').count()
    mixing_projects = MusicProject.objects.filter(status='MIXING').count()
    mastering_projects = MusicProject.objects.filter(status='MASTERING').count()
    released_projects = MusicProject.objects.filter(status='RELEASED').count()
    total_tasks = Task.objects.count()

    unfinished_tasks = Task.objects.exclude(
        status='DONE'
    ).count()

    status_labels = [
        'Idea',
        'In Progress',
        'Mixing',
        'Mastering',
        'Released',
    ]

    status_values = [
        idea_projects,
        in_progress_projects,
        mixing_projects,
        mastering_projects,
        released_projects,
    ]

    chart = None

    if sum(status_values) > 0:
        fig, ax = plt.subplots(figsize=(7, 5))

        ax.pie(
            status_values,
            labels=status_labels,
            autopct='%1.1f%%',
            startangle=90,
        )

        ax.set_title('Project Status Distribution')
        ax.axis('equal')

        buffer = io.BytesIO()
        fig.savefig(
            buffer,
            format='png',
            bbox_inches='tight',
        )
        plt.close(fig)

        buffer.seek(0)
        chart = base64.b64encode(
            buffer.getvalue()
        ).decode('utf-8')
        buffer.close()

    context = {
        'total_projects': total_projects,
        'total_tasks': total_tasks,
        'unfinished_tasks': unfinished_tasks,
        'idea_projects': idea_projects,
        'in_progress_projects': in_progress_projects,
        'mixing_projects': mixing_projects,
        'mastering_projects': mastering_projects,
        'released_projects': released_projects,
        'genre_stats': genre_stats,
        'genre_analysis': genre_analysis.to_dict(),
        'chart': chart,
    }

    return render(
        request,
        'analytics/dashboard.html',
        context
    )
