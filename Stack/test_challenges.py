import unittest
from reverseStack import *

class TestChallenges(unittest.TestCase):
	def test_reverse(self):
		self.assertEqual("yeH", reverse("Hey"))
		self.assertEqual("", reverse(""))
		self.assertEqual("54321", reverse("12345"))