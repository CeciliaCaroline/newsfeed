import unittests

class commentTestCase(unittest.TestCase):

    
    def setUp(self):

        self.comment = Comment('have fun', 9)

    def test_comment_created(self):
        """Should test if the feed has been created successfully"""
        self.assertIsInstance(self.comment, Comment)
        




if __name__ == '__main__':
    unittest.main()