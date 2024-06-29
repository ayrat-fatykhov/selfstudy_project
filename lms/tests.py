from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from lms.models import Chapter, Material, Question, Answer
from users.models import User


class MaterialTestCase(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()

        self.user = User.objects.create(id=1, email='test@sky.pro', password='1234567', is_staff=True)
        self.client.force_authenticate(user=self.user)

        self.question = Question.objects.create(question='is_test?', right_answer='yes')
        self.answer = Answer.objects.create(user=self.user, question=self.question, user_answer='yes')
        self.chapter = Chapter.objects.create(name='test_chapter', description='test_description')
        self.material = Material.objects.create(
            name='test_material',
            description='test_description',
            chapter=self.chapter,
            questionnaire=self.answer
        )

    def test_create_material(self):
        data = {
            'name': 'test_material',
            'description': 'test_description',
            'chapter': self.chapter.id,
            'questionnaire': self.answer.id
        }
        url = reverse('lms:material_create')
        response = self.client.post(url, data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Material.objects.filter(name=data['name']).exists())

    def test_retrieve_material(self):
        url = reverse('lms:material_view', kwargs={'pk': self.material.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.material.name)

    def test_update_material(self):
        url = reverse('lms:material_update', kwargs={'pk': self.material.pk})
        data = {'name': 'test_material_update', 'description': 'test_description_update'}
        response = self.client.patch(url, data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.material.refresh_from_db()
        self.assertEqual(self.material.name, data['name'])

    def test_lesson_delete(self):
        response = self.client.delete(
            reverse('lms:material_delete', args=[self.material.id])
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertEqual(
            Material.objects.count(),
            0
        )
