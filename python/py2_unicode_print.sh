#!/usr/bin/env bash
set -ex

# This seems derpy only on python2

# I have yet to explain this one
python2.7 -c 'print(u"\u2603")'
python2.7 -c 'print(u"☃")'
# Works fine in python3.4
python3.4 -c 'print(u"\u2603")'
python3.4 -c 'print(u"☃")'

# Output on my machine
# ./python/py2_unicode_print.sh
#+ python2.7 -c 'print(u"\u2603")'
#☃
#+ python2.7 -c 'print(u"☃")'
#â
#+ python3.4 -c 'print(u"\u2603")'
#☃
#+ python3.4 -c 'print(u"☃")'
#☃
