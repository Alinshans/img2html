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
    parser.add_argument('-i', '--in', default=None, metavar='SRC_FILE',
                        help='the image to convert')
    parser.add_argument('-o', '--out', default=None, metavar='OUT_FILE',
                        help='output file')

    args, text = parser.parse_known_args()

    ###########################################################################
    # Modifies here to run code.

    # src_file = **source_file** (e.g. 'a.jpg')
    src_file = getattr(args, 'in')

    if src_file:

        # Sets the conversion configuration information.
        converter_config = Img2HTMLConverter(
            font_size=args.size,
            char=args.char,
            background=args.background,
            title=args.title,
            font_family=args.font,
        )

        html = converter_config.convert(src_file)

        # out_file = **output_file_name** (e.g. 'a.html')
        out_file = args.out

    ###########################################################################

        if out_file == None:
            nameRe = re.compile(r'(\w+).(\w+)')
            out_file = nameRe.search(src_file).group(1) + '.html'

        with codecs.open(out_file, 'wb', encoding='utf-8') as fp:
            fp.write(html)

    else:
        print('usage: img2html [-h] [-b #RRGGBB] [-s 1~32] [-c CHAR] [-t TITLE] [-f FONT]')
        print('                [-i SRC_FILE] [-o OUT_FILE]')
        print('Type "img2html -h" for help information')
