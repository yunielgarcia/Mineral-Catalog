from django.core.urlresolvers import reverse
from django.test import TestCase

from .models import Mineral


# Create your tests here.
class CourseViewsTest(TestCase):
    def setUp(self):
        self.mineral1 = Mineral.objects.create(
            name="Mineral One",
            image_filename="Mineral_one_file_name",
            image_caption="mineral_one_caption",
            category="Category_one",
            group="group_one"
        )
        self.mineral2 = Mineral.objects.create(
            name="Mineral Two",
            image_filename="Mineral_two_file_name",
            image_caption="mineral_two_caption",
            category="Category_two",
            group="group_two"
        )

    def test_mineral_list_view(self):
        # self.client is similar to a web browser, it lets us make request to
        # an url and gives us back the status code and html from that url
        resp = self.client.get(reverse('minerals:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral1, resp.context['minerals'])
        self.assertIn(self.mineral2, resp.context['minerals'])

    def test_mineral_detail_view(self):
        resp = self.client.get(reverse('minerals:detail', kwargs={'pk': self.mineral1.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.mineral1, resp.context['mineral_obj'])
