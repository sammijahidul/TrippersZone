from __future__ import unicode_literals
from django.test import TestCase
from django.http import HttpRequest
from django.test import SimpleTestCase
from django.urls import reverse
from .models import owner , renter
from . import views


class HomePageTests(TestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/TrippersZone/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)

    def test_home_page_contains_correct_html(self):
        response = self.client.get('/TrippersZone/')
        self.assertContains(response, '<h1>URL is correct here</h1>')

    def test_home_page_contains_incorrect_html(self):
        response = self.client.get('/TrippersZone/')
        self.assertNotContains(response, 'Hi there! I should not be on the page.')


class PostTests(TestCase):

    def setUp(self):
        StudentPost.objects.create(Spost='tase case')