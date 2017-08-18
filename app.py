#!/usr/bin/env python
"""
The  NewsFeeds Program.

Usage:
    primfeed view_feed
    primfeed post <title> <body>
    primfeed comment <postId> <title> <body>
    primfeed (-i | --interactive)
    primfeed (-h | --help | --version)

Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import sys
import cmd
from docopt import docopt, DocoptExit