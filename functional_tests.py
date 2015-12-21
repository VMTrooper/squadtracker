from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Chrome()
		self.browser.implicitly_wait(5)

	def tearDown(self):
		# Satisfied, Mike closes the web browser
		self.browser.quit()

	def test_can_start_a_squad_and_retrieve_it_later(self):
		# Mike has heard of a site for keeping track of his
		# Destiny squad mates, and he checks it out.
		self.browser.get('http://localhost:8000')
		
		# He notices the page title and header include the text
		# "Destiny SquadTracker"
		self.assertIn('Destiny SquadTracker',self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Destiny SquadTracker',header_text)
		
		# Mike enters the gamertag of one of his teammates
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a squad member name'
			)
		inputbox.send_keys('RaZaK')
		inputbox.send_keys(Keys.ENTER)
		
		# The gamertag is added to his list of teammates,
		# and it is a clickable link that will display his
		# squad mate's light level, weapons, and armor
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(
			any(row.text == 'RaZaK' for row in rows)
			)
		
		# There is still a textbox to enter more squadmates.
		# So, he adds another.
		self.fail('Finish the test!')
		
		# The page updates and both squadmates are displayed.
if __name__ == '__main__':
	unittest.main()
	# unittest.main(warnings='ignore')