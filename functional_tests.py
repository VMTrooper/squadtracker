from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Chrome()
		self.browser.implicitly_wait(5)

	def tearDown(self):
		# Satisfied, Mike closes the web browser
		self.browser.quit()

	def check_for_row_in_list_table(self, row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text,[row.text for row in rows])

	def test_can_start_a_squad_and_retrieve_it_later(self):
		# Mike has heard of a site for keeping track of his
		# Destiny squad mates, and he checks it out.
		self.browser.get('http://localhost:8000')
		
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
		inputbox.send_keys(Keys.ENTER)
		# import time
		# time.sleep(10)
		table = self.browser.find_element_by_id('id_list_table')
		
		# The gamertag is added to his list of teammates,
		# and it is a clickable link that will display his
		# squad mate's light level, weapons, and armor
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
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


		# Mike wonders whether the site will remember his list.
		# Then he sees that the site has generated a unique URL for him
		self.fail('Finish the test!')

		# Mike visits that URL - his Squad Members are still listed.
if __name__ == '__main__':
	unittest.main()
	# unittest.main(warnings='ignore')