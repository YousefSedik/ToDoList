import os 
from django.test import TestCase
from django.conf import settings
# Create your tests here.

class test(TestCase):
    
    def test_zz(self):
        key = settings.SECRET_KEY
        print(key)