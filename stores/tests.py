from django.test import TestCase
from .models import Store
# Create your tests here.

class HomeViewTests(TestCase):

	def test_home_view(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'pages/home.html')

class StoreViewTests(TestCase):
	def setUp(self):
		Store.objects.create(name="Dell Store", notes="example")
	def tearDown(self):
		Store.objects.all().delete()

	def test_list_view_connection(self):
		response = self.client.get('/store/')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'stores/store_list.html')

	def test_list_view(self):
		r = self.client.get('/store/')
		print(r)
		self.assertContains(r,'Dell Store')
		self.assertContains(r, '<a href="/store/1/">Dell Store</a>', html=True)
