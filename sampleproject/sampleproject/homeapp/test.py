from django.test import SimpleTestCase
from django.urls import resolve,reverse
from homeapp.views import allproducts

class TestURL(SimpleTestCase)

    def testurlcart(self):
        url=reverse('product_by_category',args=['demo-slug'])

        self.assertEquals(resolve(url).func,allproducts)