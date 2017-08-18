#!/usr/bin/env python
"""
The  NewsFeeds Program.

Usage:
    primfeed view_feed
    primfeed post <title> <body>
    primfeed add_comment <commentId> <body>
    primfeed viewcomment
    update_comment update_comment
    primfeed add_user <userId> <email>
    primfeed get_user
    primfeed (-i | --interactive)
    primfeed (-h | --help | --version)

Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import sys
import cmd
from docopt import docopt, DocoptExit


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


class MyInteractive (cmd.Cmd):
    intro = 'Welcome to Primitive Social A Simple Forum Platform ' + \
        ' (type help for a list of options.)'
    prompt = '(primfeed) '
    file = None

    @docopt_cmd
    def do_view_feed(self, arg):
        """Usage: view_feed"""

        print(arg)

    @docopt_cmd
    def do_post(self, arg):
        """Usage: post <title> <body>"""

        print(arg)

    @docopt_cmd
    def do_add_user(self, arg):
        """Usage: add_user <userId> <email>"""

        print(arg)

    @docopt_cmd
    def do_get_user(self, arg):
        """Usage: get_user"""

        print(arg)

    @docopt_cmd
    def do_add_comment(self, arg):
        """Usage: add_comment <commentId> <body>"""

        print(arg)

    @docopt_cmd
    def do_viewcomments(self, arg):
        """Usage: viewcomment"""

        print(arg)

    @docopt_cmd
    def do_update_comments(self, arg):
        """Usage: update_comment"""

        print(arg)

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()


opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    MyInteractive().cmdloop()

print(opt)
