## This program will seperate every 2 letter by a ':'.

#!/usr/bin/python
# Author : Shourabh Singh

a = raw_input("Please enter the MAC ADDR : ")

print ':'.join(a[i:i+2] for i in range(0,len(a),2))
