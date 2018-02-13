## This program will comment any line which has the particular keyword given by the user in the any file.

#!/usr/bin/python
#Author : Shourabh Singh

import fileinput


input = raw_input("Site you want to comment out : ")

for line in fileinput.input('hosts1',inplace=1):
    if input in line:
#    print '{0}{1}'.format('#',line.rstrip('\n'))
    print '%s%s' % ('#',line.rstrip('\n'))
    else:
    print line.rstrip('\n')
