from django.core.urlresolvers import reverse
from django.test import TestCase

from .models import Mineral


# Create your tests here.
class CourseViewsTest(TestCase):
    def setUp(self):
        self.mineral1 = Mineral.objects.create(
            name="A Mineral One",
            image_filename="Mineral_one_file_name",
            image_caption="mineral_one_caption",
            category="Category_one",
            group="group one"
        )
        self.mineral2 = Mineral.objects.create(
            name="B Mineral Two",
            image_filename="Mineral_two_file_name",
            image_caption="mineral_two_caption",
            category="Category_two",
            group="group two"
        )

    def test_mineral_list_view(self):
        """By default mineral starting with 'A'"""
        # self.client is similar to a web browser, it lets us make request to
        # an url and gives us back the status code and html from that url
        resp = self.client.get(reverse('minerals:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral1, resp.context['minerals'])
        self.assertNotIn(self.mineral2, resp.context['minerals'])

    def test_mineral_list_view_with_initial(self):
        """Mineral starting with 'B'"""
        # self.client is similar to a web browser, it lets us make request to
        # an url and gives us back the status code and html from that url
        resp = self.client.get(reverse('minerals:list', kwargs={'initial': 'B'}))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral2, resp.context['minerals'])
        self.assertNotIn(self.mineral1, resp.context['minerals'])

    def test_mineral_list_view_with_group(self):
        """Mineral by group name"""
        # self.client is similar to a web browser, it lets us make request to
        # an url and gives us back the status code and html from that url
        resp = self.client.get(reverse('minerals:group', kwargs={'group': 'group_one'}))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral1, resp.context['minerals'])
        self.assertNotIn(self.mineral2, resp.context['minerals'])

    def test_mineral_list_view_with_search_param(self):
        """Mineral by group name"""
        # self.client is similar to a web browser, it lets us make request to
        # an url and gives us back the status code and html from that url

        resp = self.client.get(reverse('minerals:search'), {'q': 'One'})
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral1, resp.context['minerals'])
        self.assertNotIn(self.mineral2, resp.context['minerals'])

    def test_mineral_detail_view(self):
        resp = self.client.get(reverse('minerals:detail', kwargs={'pk': self.mineral1.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.mineral1, resp.context['mineral_obj'])
