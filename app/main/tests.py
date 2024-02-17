from django.test import TestCase
from django.urls import reverse

class HomePageTests(TestCase):
    def test_home_page_status_code(self):
        url = reverse('home')  # Replace 'home' with your home page URL name
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
        