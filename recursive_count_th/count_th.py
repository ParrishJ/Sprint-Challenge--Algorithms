'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    occurances = 0

    if len(word) == 0:
        return occurances
    
    def helper(word):
        
        nonlocal occurances
        if len(word) < 2:
            return

        elif len(word) >=2:
            substr = word[0] + word[1]

            if substr == 'th':
                occurances += 1
                new_word = word[2:]
               
                return helper(new_word)
            else:
                new_word = new_word = word[1:]
               
                return helper(new_word)
         
    helper(word) 
    return occurances


print(count_th('thabcthabc'))