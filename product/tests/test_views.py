from django.test import TestCase,Client
from product.models import Category,Product,Cart,WishList,TimeStamp
from django.urls import reverse

class TestViews(TestCase):
    def test_add_to_wishlist_GET(self):
        client = Client()

        response = client.get(reverse('user_wishlist'))

        self.assertEquals(response.status_code,200)
        


