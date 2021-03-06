from django.test import TestCase
from .models import Image

# Create your tests here.
class ImageTestClass(TestCase):
    #set up method
    def setUp(self):
        self.office = Image(image='office',name='apartment',description='executive')

    def test_instance(self):
        self.assertTrue(isinstance(self.office,Image))


    # Testing Save Method
    def test_save_method(self):
        self.office.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)


     # Testing delete Method
    def test_delete_method(self):
        self.office.save_image()
        record = Image.objects.all()
        self.office.delete_image()
        self.assertTrue(len(record)== 0)

