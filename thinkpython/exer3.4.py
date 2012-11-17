# def do_twice(f):
    # f()
    # f()
# 
# def print_spam():
    # print 'spam'

def do_twice(f,n):
    f(n)
    f(n)

def print_spam(n):
    print 'spam'* n

def print_twice(s):
    print s
    print s

do_twice(print_twice,'spam')
