from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page

# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')#resolve described in Evernote
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        #print("expected_html:",len(expected_html))
        #print("response: ", type(response))
        self.assertEqual(response.content.decode(), expected_html)
        #self.assertTrue(response.content.startswith(b'<html>'))
        #self.assertIn(b'<title>To-Do lists</title>', response.content)
        #self.assertTrue(response.content.strip().endswith(b'</html>'))

