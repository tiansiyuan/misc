#!/usr/bin/env python

"""to help tx ACS-DOCS"""

import os
import operator
import subprocess
import shlex
# from pprint import pprint

pathname = '/home/tian/projects/csdocs/translations'
en_dict = dict()

for i in os.listdir(pathname):
    if os.path.isdir(pathname+'/'+i) and i[:9]=='ACS_DOCS.':
        dirs = os.listdir(pathname+'/'+i)
        if ('en.po' in dirs) and ('zh_CN.po' not in dirs):
           en_dict[ i[9:] ] = os.path.getsize(pathname+'/'+i+'/'+'en.po')

sorted_en = sorted(en_dict.iteritems(), key=operator.itemgetter(1))
length = len(sorted_en)
print "%d items left." % length

#pprint(sorted_en)

n = length - 1
while n >= 0:
    print n, sorted_en[n]
    n -= 1

while True:
    num = int(raw_input("Please input the item no.: "))
    if num >= 0 and num < length:
        item = sorted_en[num][0]
        # args = shlex.split(["txpush","%s" % item ])
        subprocess.Popen(["txpush","%s" % item ]).wait()
    else:
        break
