from django.test import TestCase
from .models import Image

# Create your tests here.
class ImageTestClass(TestCase):
    #set up method
    def setUp(self):
        self.office = Image(image='office',name='apartment',description='executive')

    def test_instance(self):
        self.assertTrue(isinstance(self.office,Image))