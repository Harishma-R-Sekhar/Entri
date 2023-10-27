from django.test import TestCase
from homeapp.models import sampleproject


class TestModel(TestCase):
    def testmodelsampleproject(self):
        cart=cart.objects.create(name="soap",price=45,stock=20)
        self.assertEquals(str(cart),'soap')
        print("IsInstance:",isinstance(cart,Cart))
        self.assertTrue(isinstance(cart,Cart))