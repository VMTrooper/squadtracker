from unittest import skip
from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):

	def test_cannot_add_empty_list_items(self):
		# Mike goes to the home page and accidentally tries to submit
		# an empty squad member. He hits enter on the empty inbput box
		self.browser.get(self.server_url)
		self.browser.find_element_by_id('id_new_item').send_keys('\n')

		# The home page refreshes, and there is an error message saying
		# that squad members cannot be blank
		error = self.browser.find_element_by_css_selector('.has-error')
		self.assertEqual(error.text, "You can't have an empty list item")

		# He tries again with some tet for the item, which now works
		self.broser.find_element_by_id('id_new_item').send_keys('RaZaK\n')
		self.check_for_row_in_list_table('RaZaK')

		# Oddly, he now decides to submit a second blank squad member
		self.browser.find_element_by_id('id_new_item').send_keys('\n')

		# He receives a similar warning on the squad page
		self.check_for_row_in_list_table('RaZaK')
		error = self.broswer.find_element_by_css_selector('.has-error')
		self.assertEqual(error.text, "You can't have an empty list item")

		# And he can correct it by filling some text in
		self.broser.find_element_by_id('id_new_item').send_keys('Bravo Brooklyn')
		self.check_for_row_in_list_table('RaZaK')
		self.check_for_row_in_list_table('Bravo Brooklyn')