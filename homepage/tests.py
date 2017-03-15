from django.test import TestCase

class testingstuff(TestCase):

	def testingmath(self):
		x=3+4
		self.assertIs(x==7, True)

	def testingmoremath(self):
		x=4+4
		self.assertIs(x==8, True)

	def testingevenmoremath(self):
		x=5+4
		self.assertIs(x==9, True)

	def testingevenmoremath2(self):
		x=9+9
		self.assertIs(x==19, False)

	def testagain(self):
		x=5
		self.assertIs(x==5, True)


# Create your tests here.
