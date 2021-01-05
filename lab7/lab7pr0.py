'''Jonathan Licht
Lab 7 part 0'''

def uppercount(s):
    capital_letters = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    if s == '':                                     #base case
        return 0   
    else:                                           #recursive case
        if s[0] in capital_letters:
            return uppercount(s[1:]) + 1
        else:
            return uppercount(s[1:])

'''can be used to look at how many sentences are in a file
(assuming no proper nouns)
can be used to count how many proper nouns there are
(assuming it is only one sentence)
'''


def clean_string(s):
    char = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm '
    if s == '':                                     #base case
        return s
    else:                                           #recursive case
        if s[0] in char:
            return s[0] + clean_string(s[1:])
        else:
            return clean_string(s[1:])

def clean_list(l1, l2):
    if l1 == []:                                    #base case
        return l1
    else:                                           #recursive case
        if l1[0] not in l2:
            return [l1[0]] + clean_list(l1[1:], l2)
        else:
            return clean_list(l1[1:], l2)

print(uppercount("Hello, World"))
print(clean_string("Hello, World"))
print(clean_list([1,2,3,4,5,6,7], [2,4,6]))
 
