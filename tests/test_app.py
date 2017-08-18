import unittests
import os

class appCase(unittest.TestCase):
    @classmethod
    def setUp(self):

        self.user = User{"1A","team1@gmail.com"}
        


    def test_user_add(self):
        """Should test that user is created successfully"""
        self.assertTrue(self.user)

    
    def test_get_user(self):
        """  Pick the user"""
        self.user = User('1A')
        self.assertIsInstance(self.user.get_lists(), list)
        self.assertEqual(len(self.user.get_lists()), 2)


        if __name__ == '__main__':
            unittest.main()