#!/usr/bin/env python

#-*- coding: utf-8 -*-

"""to help tx ACS-DOCS"""

import os
import operator
import subprocess
import shlex
import polib
# from pprint import pprint

pathname = '/home/tian/projects/csdocs/translations'
en_dict = dict()

def get_msgstr(i):
    """use polib to get msgstrs of each en.po file;
    and put them into one file;
    upload the file to google translate;
    insert the translation into zh_CN.pl files.
    use tag to separate msgstrs
    after cp en.po zh_CN.po, use polib to replace msgstr in zh_CN.po with translation.
    before tx push, use vi to have a look.
    """
    po = polib.pofile(pathname+'/ACS_DOCS.'+i+'/'+'en.po')
    
    # print 'processing %s' % i

    print "<begin %s>\n" % i

    for entry in po:
        print entry.msgstr
        # msgstrfile.write(entry.msgstr)
        print '\n'

    print "<end %s>\n" % i

for i in os.listdir(pathname):
    if os.path.isdir(pathname+'/'+i) and i[:9]=='ACS_DOCS.':
        dirs = os.listdir(pathname+'/'+i)
        if ('en.po' in dirs) and ('zh_CN.po' not in dirs):
           en_dict[ i[9:] ] = os.path.getsize(pathname+'/'+i+'/'+'en.po')

sorted_en = sorted(en_dict.iteritems(), key=operator.itemgetter(1))

# msgstrfile=open(pathname+'/../msgstr.txt', 'w')

for i in sorted_en:
    get_msgstr(i[0])

# msgstrfile.close()

"""
length = len(sorted_en)
print "%d items left." % length

n = length - 1
while n >= 0:
    print n, sorted_en[n]
    n -= 1

while True:
    num = int(raw_input("Please input the item no.(0 - %d), anything else to quit: " % (length -1) ))
    if num >= 0 and num < length:
        item = sorted_en[num][0]
        # args = shlex.split(["txpush","%s" % item ])
        subprocess.Popen(["txpush","%s" % item ]).wait()
    else:
        break

"""
