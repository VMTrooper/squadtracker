from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(FunctionalTest):

	def test_can_start_a_squad_and_retrieve_it_later(self):
		# Mike has heard of a site for keeping track of his
		# Destiny squad mates, and he checks it out.
		self.browser.get(self.server_url)
		
		# He notices the page title and header include the text
		# "Destiny SquadTracker"
		self.assertIn('Destiny SquadTracker',self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Destiny Squad',header_text)
		
		# Mike enters the gamertag of one of his teammates
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a squad member name'
			)
		inputbox.send_keys('RaZaK')

		# When he hits enter, he is taken to a new URL,
		# and now the page lists "RaZaK" as a member in the
		# Squad table.
		inputbox.send_keys(Keys.ENTER)
		mike_list_url = self.browser.current_url
		self.assertRegex(mike_list_url, 'squads/.+')
		self.check_for_row_in_list_table('RaZaK')

		# There is still a textbox to enter more squadmates.
		# So, he adds another.
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Bravo Brooklyn')
		inputbox.send_keys(Keys.ENTER)

		# The page updates and both squadmates are displayed.
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.check_for_row_in_list_table('RaZaK')
		self.check_for_row_in_list_table('Bravo Brooklyn')

		# Now a new user, Johnny, comes along to the site.

		## We use a new browser session to make sure that no information
		## of Mike's is coming through from cookies, etc.
		self.browser.quit()
		self.browser = webdriver.Chrome()

		# Johnny visits the home page. There is no sign of Mike's
		# list
		self.browser.get(self.server_url)
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Bravo Brooklyn',page_text)
		self.assertNotIn('RaZaK',page_text)

		# Johnny starts a new list by entering a new item. He
		# has less squad members than Mike
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('PR Dragon')
		inputbox.send_keys(Keys.ENTER)

		# Johnny gets his own unique URL
		johnny_list_url = self.browser.current_url
		self.assertRegex(johnny_list_url, '/squads/.+')
		self.assertNotEqual(johnny_list_url, mike_list_url)

		# Again, there is no trace of Mike's list
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Bravo Brooklyn', page_text)
		self.assertIn('PR Dragon', page_text)

		# Satisfied, they both go back to Destiny