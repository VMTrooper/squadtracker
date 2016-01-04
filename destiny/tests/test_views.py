from django.test import TestCase
from django.http import HttpRequest, HttpResponse
from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from destiny.views import home_page
from destiny.models import Item, List

class NewItemTest(TestCase):
	def test_can_save_a_POST_request_to_an_existing_list(self):
		other_list = List.objects.create()
		correct_list = List.objects.create()

		self.client.post(
			'/squads/%d/add_item' % (correct_list.id,),
			data={'item_text': 'A new member for an existing squad'})
		self.assertEqual(Item.objects.count(),1)
		new_item = Item.objects.first()
		self.assertEqual(new_item.text, 'A new member for an existing squad')
		self.assertEqual(new_item.list, correct_list)
	def test_redirects_to_list_view(self):
		other_list = List.objects.create()
		correct_list = List.objects.create()

		response = self.client.post(
			'/squads/%d/add_item' % (correct_list.id,),
			data={'item_text': 'A new member for an existing squad'})
		self.assertRedirects(response, '/squads/%d/' % (correct_list.id,))

class NewListTest(TestCase):
	def test_redirects_after_POST(self):
		response = self.client.post('/squads/new',
			data={'item_text': 'A new squad member'})
		new_list = List.objects.first()
		self.assertRedirects(response, '/squads/%d/' % (new_list.id,))

	def test_saving_a_POST_request(self):
		self.client.post('/squads/new',
			data={'item_text': 'A new squad member'})

		self.assertEqual(Item.objects.count(), 1)
		new_item = Item.objects.first()
		self.assertEqual(new_item.text,'A new squad member')

class ListViewTest(TestCase):
	def test_passes_correct_list_to_template(self):
		other_list = List.objects.create()
		correct_list = List.objects.create()
		response = self.client.get('/squads/%d/' % (correct_list.id,))
		self.assertEqual(response.context['squad'], correct_list)

	def test_uses_list_template(self):
		list_ = List.objects.create()
		response = self.client.get('/squads/%d/' % (list_.id,))
		self.assertTemplateUsed(response, 'list.html')

	def test_displays_only_items_for_that_list(self):
		correct_list = List.objects.create()
		Item.objects.create(text='squadmem01', list=correct_list)
		Item.objects.create(text='squadmem02', list=correct_list)
		other_list = List.objects.create()
		Item.objects.create(text='other squadmem01', list=other_list)
		Item.objects.create(text='other squadmem02', list=other_list)

		response = self.client.get('/squads/%d/' % (correct_list.id,))

		self.assertContains(response, 'squadmem01')
		self.assertContains(response, 'squadmem02')
		self.assertNotContains(response, 'other squadmem01')
		self.assertNotContains(response, 'other squadmem02')

class HomePageTest(TestCase):
	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		expected_html = render_to_string('home.html')
		self.assertEqual(response.content.decode(), expected_html)