## Read a file to find the longest palindrome in it.
## 2 different functions..Use any

import string

file = '/tmp/file.txt'

def palindrome_using_var(file):
    long_pal = ''
    content = open(file, 'r').read()
    no_punc_content = content.translate(None, string.punctuation)
    split_content = no_punc_content.split()

    for word in split_content:
        if word == word[::-1]:
  	    if len(long_pal) < len(word) :
	       long_pal = word
    print long_pal


def palindrome_using_list(file):
    list_pal = []
    long_pal = ''
    content = open(file, 'r').read()
    no_punc_content = content.translate(None, string.punctuation)
    split_content = no_punc_content.split()

    for word in split_content:
        if word == word[::-1]:
            list_pal.append(word)

    for i in list_pal:
        if len(i) > len(long_pal):
	    long_pal = i

    print list_pal
    print long_pal

palindrome_using_list(file)

