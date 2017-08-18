import unittests

class feeTestCase(unittest.TestCase):

    
    def setUp(self):

        self.feed = Feed('Trip','travelling to China',2)
        self.comment = Comment('have fun', 9)

    def test_feed_created(self):
        """Should test if the feed has been created successfully"""
        self.assertIsInstance(self.feed, Feed)
        

def test_create_comment(self):
        """Should check if  succesfully added feed"""
        self.user.add_comment(self.comment)

def test_update_comment(self):
        """Should test for updating the a comment"""
        self.user.create_comment(self.comment)
        new_comment_body = ''
        new_comment_id = ''
        self.user.update_feed(self.comment.body,new_comment_body )
        self.assertEqual(self.comment.body, new_comment_body)


if __name__ == '__main__':
    unittest.main()