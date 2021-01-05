string = 'yo mama'

def countVowels(s):
    counter = 0
    vowels = 'aeiouAEIOU'
    for i in s:
        if i in vowels:
            counter += 1
    return counter
        
print(countVowels(string))
