#!/usr/bin/env python
# encoding=utf-8

from __future__ import print_function, unicode_literals

import argparse
import codecs
import re

from img2html.converter import Img2HTMLConverter

def main():
    parser = argparse.ArgumentParser(description='img2html : Converts the image to HTML')
    parser.add_argument('-b', '--background', default='000000', metavar='#RRGGBB',
                        help='background color (#RRGGBB format)')
    parser.add_argument('-s', '--size', default=4, type=int, metavar='(1~32)',
                        help='text font size (int)')
    parser.add_argument('-c', '--char', default='爱', metavar='CHAR',
                        help='characters for HTML text')
    parser.add_argument('-t', '--title', default='Image', metavar='TITLE',
                        help='html title')
    parser.add_argument('-f', '--font', default='monospace', metavar='FONT',
                        help='html font')
    parser.add_argument('-i', '--in', default=None, metavar='IN',
                        help='the image to convert')
    parser.add_argument('-o', '--out', default=None, metavar='OUT',
                        help='output file')

    args, text = parser.parse_known_args()

    src_file = getattr(args, 'in')

    if src_file:

        ###########################################################################
        # Modifies here to run code.

        # Sets the conversion configuration information.
        converter_config = Img2HTMLConverter(
            font_size=args.size,
            char=args.char,
            background=args.background,
            title=args.title,
            font_family=args.font,
        )

        # html = converter_config.convert(**source_file**) (e.g. 'a.JPG')
        html = converter_config.convert(getattr(args, 'in'))

        # out_file = **output_file_name** (e.g. 'a.html')
        out_file = args.out

        ###########################################################################
        if out_file == None:
            nameRe = re.compile(r'(\w)+.(\w)+')
            out_name = nameRe.search(getattr(args, 'in')).group(1) + '.html'

        with codecs.open(out_file, 'wb', encoding='utf-8') as fp:
            fp.write(html)
