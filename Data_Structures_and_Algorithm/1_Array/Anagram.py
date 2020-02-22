
## Check the anagram i.e. 2 words are created with same letters (e.g 'god' and 'dog')

## 1st Method
def anagram1(s1,s2):

    ## Remove whitespaces
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()

    return sorted(s1) == sorted(s2)

## 2nd Method
def anagram2(s1, s2):

    ## Remove whitespaces
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    ## Edge case check
    if len(s1) != len(s2):
        return False

    count = {}

    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    print(count)

    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    print(count)

    for k in count:
        if count[k] != 0:
            return False

    return True