from django.test import TestCase
from django.urls import reverse
from .models import MusicProject, Genre
from .forms import MusicProjectForm


class MusicProjectModelTest(TestCase):
    def test_create_music_project(self):
        genre = Genre.objects.create(name='Bass House')

        project = MusicProject.objects.create(
            title='Test Music Project',
            genre=genre,
        )

        self.assertEqual(project.title, 'Test Music Project')
        self.assertEqual(project.genre.name, 'Bass House')
        self.assertEqual(MusicProject.objects.count(), 1)

class ProjectListViewTest(TestCase):
    def test_project_list_page_loads(self):
        response = self.client.get(reverse('project_list'))

        self.assertEqual(response.status_code, 200)

    def test_project_create_page_loads(self):
        response = self.client.get(reverse('project_create'))

        self.assertEqual(response.status_code, 200)

    def test_project_create_post(self):
        response = self.client.post(
            reverse('project_create'),
            {
                'title': 'Test Track',
                'status': 'IDEA',
            }
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            MusicProject.objects.filter(title='Test Track').exists()
        )


    def test_project_detail_page_loads(self):
        project = MusicProject.objects.create(
            title='Detail Test Track',
            status='IDEA',
        )

        response = self.client.get(
            reverse('project_detail', kwargs={'pk': project.pk})
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Detail Test Track')


    def test_project_edit_page_loads(self):
        project = MusicProject.objects.create(
            title='Edit Test Track',
            status='IDEA',
        )

        response = self.client.get(
            reverse('project_edit', kwargs={'pk': project.pk})
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Edit Test Track')


    def test_project_edit_post(self):
        project = MusicProject.objects.create(
            title='Old Track Name',
            status='IDEA',
        )

        response = self.client.post(
            reverse('project_edit', kwargs={'pk': project.pk}),
            {
                'title': 'Updated Track Name',
                'status': 'IN_PROGRESS',
            }
        )

        project.refresh_from_db()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(project.title, 'Updated Track Name')
        self.assertEqual(project.status, 'IN_PROGRESS')


    def test_project_delete(self):
        project = MusicProject.objects.create(
            title='Track To Delete',
            status='IDEA',
        )

        response = self.client.post(
            reverse('project_delete', kwargs={'pk': project.pk})
        )

        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            MusicProject.objects.filter(pk=project.pk).exists()
        )


    def test_task_create_page_loads(self):
        project = MusicProject.objects.create(
            title='Task Test Track',
            status='IDEA',
        )

        response = self.client.get(
            reverse('task_create', kwargs={'pk': project.pk})
        )

        self.assertEqual(response.status_code, 200)


    def test_note_create_page_loads(self):
        project = MusicProject.objects.create(
            title='Note Test Track',
            status='IDEA',
        )

        response = self.client.get(
            reverse('note_create', kwargs={'pk': project.pk})
        )

        self.assertEqual(response.status_code, 200)


    def test_track_version_create_page_loads(self):
        project = MusicProject.objects.create(
            title='Version Test Track',
            status='IDEA',
        )

        response = self.client.get(
            reverse('track_version_create', kwargs={'pk': project.pk})
        )

        self.assertEqual(response.status_code, 200)


    def test_project_search(self):
        MusicProject.objects.create(
            title='Deep Bass Track',
            status='IDEA',
        )
        MusicProject.objects.create(
            title='Melodic House Track',
            status='IDEA',
        )

        response = self.client.get(
            reverse('project_list'),
            {'search': 'Deep Bass'},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Deep Bass Track')
        self.assertNotContains(response, 'Melodic House Track')


    def test_project_status_filter(self):
        MusicProject.objects.create(
            title='Active Track',
            status='IN_PROGRESS',
        )
        MusicProject.objects.create(
            title='Idea Track',
            status='IDEA',
        )

        response = self.client.get(
            reverse('project_list'),
            {'status': 'IN_PROGRESS'},
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Active Track')
        self.assertNotContains(response, 'Idea Track')


    def test_project_list_pagination(self):
        for number in range(7):
            MusicProject.objects.create(
                title=f'Pagination Track {number}',
                status='IDEA',
            )

        response = self.client.get(reverse('project_list'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['projects']), 6)
        self.assertTrue(response.context['page_obj'].has_next())


class MusicProjectFormTest(TestCase):
    def test_title_is_required(self):
        form = MusicProjectForm(data={
            'title': '',
            'description': '',
            'genre': '',
            'status': 'IDEA',
            'bpm': '',
            'musical_key': '',
            'release_date': '',
            'duration': '',
            'cover': '',
        })

        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)
