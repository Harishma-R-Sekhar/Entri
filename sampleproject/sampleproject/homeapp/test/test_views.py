from django.test import TestCase,Client
from django.urls import reverse,resolve

class TestViews(TestCase):

    def test_views(self):
        client=Client()
        response=client.get(reverse('cart'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'cart_list.html')