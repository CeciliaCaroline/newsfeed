import unittest

class Test_Feed(unittest.TestCase):
	def add_feed(self):
	"""test that should not be an empty string, should not be none and should be a string"""
		self.foo = Feed()
        	self.failUnlessRaises(IndexError, foo.feed_is_invalid, '')
        	self.failUnlessRaises(TypeError, foo.feed_is_invalid, None)

	def view_feed(self):
	"""test to make sure feed is displayed as string"""
		self.foo= Feed()
		self.failUnlessRaises(TypeError, foo.feed_is_invalid, 234)

if __name__ = '__main__':
	unittest.main()
