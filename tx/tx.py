#!/usr/bin/env python

#-*- coding: utf-8 -*-

"""to help tx ACS-DOCS"""

import os
import operator
import subprocess
import shlex
import polib
import shutil
# from pprint import pprint

pathname = '/home/tian/projects/csdocs/translations'
en_dict = dict()

def get_msgstr(i):
    """use polib to get msgstrs of each en.po file;
    and put them into one file;
    upload the file to google translate;
    insert the translation into zh_CN.pl files,
    using double blank lines to separate msgstrs;
    cp en.po zh_CN.po,;
    use polib to replace msgstr in zh_CN.po with translation;
    before tx push, use vi to have a check and modify if needed.

    """
    po = polib.pofile(pathname+'/ACS_DOCS.'+i+'/'+'en.po')
    
    # print 'processing %s' % i

    print "<begin %s>\n" % i

    for entry in po:
        print entry.msgstr
        # msgstrfile.write(entry.msgstr)
        print '\n'

    print "<end %s>\n" % i

def get_trans(item):
    """
    1. find "<begin item>" in transfile;
    2. get the content until "<end item>";
    3. replace corresponding msgstr with substracted content;
    """
    transfile=open(pathname+'/../msgstr_cn.txt')
    matched = False # indicator of if the matched section if found.
    result = []

    lines=transfile.readlines()

    for line in lines:
        line = line.rstrip()

        if matched:
            if line == '<end ' + item + '>':
                matched = False
            else:
                result.append(line)
        else:
            if line == '<begin ' + item + '>':
                matched = True
            
    transfile.close()

    # sort out result
    # replace msgstr with translation
    # po = polib.pofile(pathname+'/ACS_DOCS.' + item + '/'+'zh_CN.po')

    # to make thing simple, just append the content of result to the end of zh_CN.po

    with open(pathname+'/ACS_DOCS.' + item + '/'+'zh_CN.po', "a") as pofile:
        pofile.write('------------\n')
        for i in result:
            pofile.write(i+'\n')

    pofile.close()


# end of get_trans()

# beginning of main()

for i in os.listdir(pathname):
    if os.path.isdir(pathname+'/'+i) and i[:9]=='ACS_DOCS.':
        dirs = os.listdir(pathname+'/'+i) # list the content of this dir
        if ('en.po' in dirs) and ('zh_CN.po' not in dirs): # item (dir) without Chinese translation
           en_dict[ i[9:] ] = os.path.getsize(pathname+'/'+i+'/'+'en.po')

sorted_en = sorted(en_dict.iteritems(), key=operator.itemgetter(1))

"""
to get original msgstr from en.po files and write into ONE file 
for later uploading to google translate manually.

# msgstrfile=open(pathname+'/../msgstr.txt', 'w')

for i in sorted_en:
    get_msgstr(i[0])


# msgstrfile.close()

"""


length = len(sorted_en)
print '    %d items left.\n' % length

n = length - 1
while n >= 0:
    print n, sorted_en[n]
    n -= 1

while True:
    num = int(raw_input("Please input the item no.(0 - %d), any other number to quit: " % (length -1) ))
    if num >= 0 and num < length:
        item = sorted_en[num][0]
        popath = pathname + '/ACS_DOCS.' + item +'/'

        if os.path.exists(popath + 'zh_CN.po.bak'):
            shutil.move(popath + 'zh_CN.po.bak', popath + 'zh_CN.po')
        else:
            shutil.copyfile(popath + 'en.po', popath + 'zh_CN.po')
            get_trans(sorted_en[num][0])

        # use vi to manually check and modify zh_CN.po
        subprocess.Popen(["vi","%s" % popath + 'zh_CN.po' ]).wait()

        # final confirmation if to push back
        confirmation = raw_input("Push back the translation, Y/N?")

        if confirmation == 'Y' or confirmation == 'y' :
            # tx push -l zh_CN -r ACS_DOCS.$1 -t
            print "trying: tx push -l zh_CN -r ACS_DOCS.%s -t" % item
            subprocess.Popen(["tx", "push -l zh_CN -r ACS_DOCS.%s -t" % item ]).wait()
        else:
            shutil.move(popath + 'zh_CN.po', popathname + 'zh_CN.po.bak')
            print('translation of %s is not pushed back, it is backed up in the same dir.' % item)
    else:
        break


