str = raw_input('Please input a string >')

def rev_str(s):
    if len(s) <= 1:
        return s
    else:
        return s[-1] + rev_str(s[:-1])

print 'reversed string is:', rev_str(str)
