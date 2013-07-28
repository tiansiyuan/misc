#!/usr/bin/python

from fabric.api import run

def host_os():
    run('uname -s')
