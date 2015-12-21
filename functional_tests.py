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
		self.fail('Finish the test!')
		
		# Mike enters the gamertag of one of his teammates
		
		# The gamertag is added to his list of teammates,
		# and it is a clickable link that will display his
		# squad mate's light level, weapons, and armor
		
		# There is still a textbox to enter more squadmates.
		# So, he adds another.
		
		# The page updates and both squadmates are displayed.
if __name__ == '__main__':
	unittest.main()
	# unittest.main(warnings='ignore')