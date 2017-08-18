#!/usr/bin/env python
"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.
Usage:
    newsfeed.py view_feed
    newsfeed.py add_post <title> <body>
    newsfeed.py (-i | --interactive)
    newsfeed.py (-h | --help | --version)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import sys
import cmd
from docopt import docopt, DocoptExit
# from afeed import NewsFeed
import requests


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class MyInteractive(cmd.Cmd):
    intro = 'Welcome to my interactive program!' \
            + ' (type help for a list of commands.)'
    prompt = '(News Feed) '
    file = None

    @docopt_cmd
    def do_view_feed(self, arg):
        """Usage: view_feed"""
        get_url = "http://34.207.10.230:3000/posts"
        response = requests.get(get_url)
        if response.status_code == 200:
            result = response.json()
            for post in result:
                title = post.get('title')
                body = post.get('body')
                id = post.get('id')
                if title is not None:
                    print('id: ', id)
                    print('title:', title)
                    print('body: ', body)
                    print('********************************')

    @docopt_cmd
    def do_primfeed_post(self, arg):
        pass

    @docopt_cmd
    def do_primfeed_comment(self, arg):
        pass

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()


opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    MyInteractive().cmdloop()

print(opt)
