from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from unittest import skip

class ItemValidationTest(FunctionalTest):

	def test_cannot_add_empty_list_items(self):
		# Mike goes to the home page and accidentally tries to submit
		# an empty squad member. He hits enter on the empty inbput box

		# The home page refreshes, and there is an error message saying
		# that squad members cannot be blank

		# He tries again with some tet for the item, which now works

		# Oddly, he now decides to submit a second blank squad member

		# He receives a similar warning on the squad page

		# And he can correct it by filling some text in
		self.fail('write me!')