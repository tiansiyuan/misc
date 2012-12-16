#!/usr/bin/env python

"""to help tx ACS-DOCS"""

import os
import operator
from pprint import pprint

pathname = '/home/tian/projects/csdocs/translations'
en_dict = dict()

for i in os.listdir(pathname):
    if os.path.isdir(pathname+'/'+i) and i[:9]=='ACS_DOCS.':
        dirs = os.listdir(pathname+'/'+i)
        if ('en.po' in dirs) and ('zh_CN.po' not in dirs):
           en_dict[ i[9:] ] = os.path.getsize(pathname+'/'+i+'/'+'en.po')

sorted_en = sorted(en_dict.iteritems(), key=operator.itemgetter(1))
pprint(sorted_en)
