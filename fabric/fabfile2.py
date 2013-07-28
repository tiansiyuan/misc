#!/usr/bin/python
# -*- coding: utf-8 -*-
from fabric.api import *
import string
from random import choice
import socket
import paramiko

env.user = 'root'
env.password = 'root'
env.hosts = [ 'grid00', 'grid01', 'grid02', 'grid03', 'grid04', 'grid05']

@task
@parallel
def passwd(user, passwd=False):
    with settings(hide('running', 'stdout', 'stderr'), warn_only=True):
        if isup(env.host):
            if not passwd:
                passwd = genpass()
            sudo("echo -e '%s\n%s' | passwd %s" % (passwd, passwd, user))

def genpass(length=10):
    return ''.join(choice(string.ascii_letters + string.digits) for _ in range(length))

def isup(host):
    print 'connecting host: %s' % host
    timeout = socket.getdefaulttimeout()
    socket.setdefaulttimeout(1)
    up = True
    try:
        paramiko.Transport((host, 22))
    except Exception, e:
        up = False
        print '%s down, %s' % (host, e)
    finally:
        socket.setdefaulttimeout(timeout)
        return up
