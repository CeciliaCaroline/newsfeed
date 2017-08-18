#newsfeed.py

"""
Class created on 18/08/2017 by Isaac Ssekamatte.
Used to make the NewsFeed object in the Andela BootCamp UG3-Newsfeed group App
"""

class NewsFeed():
    """
    News Feed Class
    Has only two methods to add and Remove Comment
    Its intantiated with a newsfeed title and body and they be null
    """
    def __init__(self, title, body):
        self.comments = []
        self.title = title
        self.body = body

    def add_comment(self, commnent):
        """
        Add comment to news feed
        """
        self.comments.append(commnent)

    def update_comment(self, new_comment, old_comment_index):
        """
        Replaces Comment with "old_comment index" with new_commnent
        """
        self.comments[old_comment_index] = new_comment
        