from django.shortcuts import render
from projects.models import MusicProject, Task
from django.db.models import Count

from django.utils.translation import gettext as _

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
            .fillna(_('No Genre'))
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
        _('Idea'),
        _('In Progress'),
        _('Mixing'),
        _('Mastering'),
        _('Released'),
    ]

    status_values = [
        idea_projects,
        in_progress_projects,
        mixing_projects,
        mastering_projects,
        released_projects,
    ]

    chart_data = [
        (label, value)
        for label, value in zip(status_labels, status_values)
        if value > 0
    ]

    chart_labels = [item[0] for item in chart_data]
    chart_values = [item[1] for item in chart_data]

    chart = None

    if sum(chart_values) > 0:
        fig, ax = plt.subplots(figsize=(7, 5))

        chart_labels = [
            label for label, value in zip(status_labels, status_values)
            if value > 0
        ]

        chart_values = [
            value for value in status_values
            if value > 0
        ]

        ax.pie(
            chart_values,
            labels=chart_labels,
            autopct='%1.1f%%',
            startangle=90,
        )

        ax.set_title(_('Project Status Distribution'))
        ax.axis('equal')

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
