'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    #base case - word is too short
    if len(word) < 2:
        return 0
    #recursion
    else:
        # if first two characters are 'th'
        if word[:2] == 'th':
            return 1 + count_th(word[2:])
        # move over one character in the word
        # pass the new word back into the function until the word is less than 0
        else:
            return count_th(word[1:])
