##

## Create a function that takes in a number as a string n and returns the number(in string format) without trailing and leading zeros.
#  You are allowed to use any language of your choice.
#  ● Trailing Zeros are the zeros after a decimal point which don't affect the value (e.g. the last three zeros in 3.4000 and 3.04000).
#  ● Leading Zeros are the zeros before a whole number which don't affect the value (e.g. the first three zeros in 000234 and 000230).
#  ● If you get a number with .0 on the end, return the integer value (e.g. return "4" rather than "4.0").
#  ● If the number is 0, 0.0, 000, 00.00, etc... return "0".
#
#  Examples:-
#  removeLeadingTrailing("230.000") ➞ "230"
#  removeLeadingTrailing("00402") ➞ "402"
#  removeLeadingTrailing("03.1400") ➞ "3.14"
#  removeLeadingTrailing("30") ➞ "30"
##

def removeLeadingTrailing(number):

    lower = None
    decimal = None
    upper = None

    for i in range(len(number)):
        if lower == None:
            if number[i]  == ".":
                decimal = i
                upper = i
                lower = i - 1
            elif number[i] != "0":
                lower = i
        else:
            if decimal == None:
                if number[i] == ".":
                    decimal = i
                    upper = i
                else:
                    upper = i + 1

            else:
                if number[i] != "0":
                    upper = i + 1

    if lower == None and upper == None:
        print "lower {} upper {} output {}".format(lower,upper,"0")
    else:
        print "lower {} upper {} output {}".format(lower,upper,number[lower:upper])


def removeLeadingTrailing1(num):

    bb = num.split('.')

    for i in bb[0]:
        if i == '0' :
            pass
        else:
            bb[0] = bb[0][bb[0].index(i):]
            break

    try:
        for i in range(len(bb[1]))[::-1]:
            if bb[1][i] == '0' :
                out = ''
                pass
            else:
                out = bb[1][0:i+1]
                break
        bb[1] = out
    except IndexError:
        pass
    print ".".join(bb)


def removeLeadingTrailing2(num):

    after_dec = ''

    for pos in range(len(num.split('.'))):
        if pos == 0:
            before_dec = list(num.split('.')[pos])
            print "before_dec", before_dec
            while (before_dec[0] == '0'):
                before_dec.pop(0)
                if not before_dec:
                    break

        elif pos == 1:
            after_dec = list(num.split('.')[pos])
            print "after_dec", after_dec
            while (after_dec[::-1][0] == '0'):
                after_dec.pop()
                if not after_dec:
                    break

    if not after_dec:
        print "".join(before_dec)
    else:
        print "".join(before_dec)+ '.' + "".join(after_dec)


def removeLeadingTrailing3(num):

    before_dec = list(num.split('.')[0])
    while (before_dec[0] == '0'):
        before_dec.pop(0)
        if not before_dec:
            break

    try:
        after_dec = list(num.split('.')[1])
        while (after_dec[::-1][0] == '0'):
            after_dec.pop()
            if not after_dec:
                break
    except IndexError:
        after_dec = ''

    if not after_dec:
        print "".join(before_dec)
    else:
        print "".join(before_dec)+ '.' + "".join(after_dec)


removeLeadingTrailing("000230.00100")
removeLeadingTrailing("0040200")
removeLeadingTrailing("03.1400")
removeLeadingTrailing("30")
removeLeadingTrailing("0.00")
removeLeadingTrailing("00")
