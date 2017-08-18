import unittest
import sys
import os

sys.path.append(os.path.abspath('../classes'))
#from calculator import simpleCalc
#from shoppinglists import SList

from user import User
from shoppinglists import SList
from items import Item


class UserCase(unittest.TestCase):
    @classmethod
    def setUp(self):

        self.user = User(''team1@gmail.com, '1A')
        self.feed = Feed('Trip','travelling to China',2)
        self.comment = Comment('have fun', 9)


    def test_user_created(self):
        """Should test that user is created successfully"""
        self.assertTrue(self.user)

    def test_create_feed(self):
        """Should check if  succesfully added feed"""
        self.user.add_feed(self.feed)
        #index = len(self.user.feed) - 1
        #self.assertEqual(self.user.feeds[index].name, 'travel')


    def test_create_feed_that_already_exists(self):
        """Should return false if feed title already exists"""
        self.user.create_feed(self.feed)
        self.assertFalse(self.user.create_feed(self.slist))

    def test_update_feed(self):
        """Should test for updating the feed"""
        self.user.create_feed(self.feed)
        new_feed_title = ''
        self.user.update_feed(self.feed.title,new_feed_title, )
        self.assertEqual(self.feed.title, new_feed_title)

    if __name__ == '__main__':
        unittest.main()
