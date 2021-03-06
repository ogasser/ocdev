#!/usr/bin/env python3
"""
ownCloud developer tool which can be used to create ownCloud apps
"""

__author__ = 'Bernhard Posselt'
__copyright__ = 'Copyright 2012-2014, Bernhard Posselt'
__license__ = 'AGPL3+'
__maintainer__ = 'Bernhard Posselt'
__email__ = 'dev@bernhard-posselt.com'


import argparse
import sys
import os

from ocdev.plugins import PLUGINS


def main():
    parser = argparse.ArgumentParser()
    parsers = parser.add_subparsers(help='commands')

    for plugin in PLUGINS:
        plugin.add_sub_parser(parsers)

    arguments = parser.parse_args()

    # get he plugin that can handle the input
    try:
        for plugin in PLUGINS:
            if plugin.can_handle(arguments.which):
                plugin.run(arguments, os.getcwd())

    except AttributeError:
        parser.print_help()
        exit(1)


if __name__ == '__main__':
    main()
