import random

# Import Text
text = './news.txt'
f = open(text, "r")
ftext = f.read()
print(f.read())

# Hammer example function
def hammer_pickOneMemeber():
    '''example function'''

    teamJDE = ['hammer', 'billy', 'chistina']
    result = random.sample(teamJDE, 1)
    return result


# Task-1 - count the total number of words in the prargraph that contains vowel characters(a, e, i, o u)
def taskOne():
    text =str( './news.txt')
    f = open(text, "r")
    tot = 0
    vowels = ['a','e','i','o','u']

    for char in f.read():
        if char in vowels:
            tot = tot +1
    f.close()

    return(f"\nTotal Vowels are: {tot}")

#Task Three
def taskThree():
    text = './news.txt'
    f = open(text, "r")
    return(f.read()[::-1])

# Task 4 (Reverse the order of character of each word e.g. I am a boy -> I ma a yob)
def taskFour(t):
    # Set up variable
    ftext = f.read()
    word_p = []
    reordered = []
    reordered_p = []
    reordered_text = ''
    reordered_all = ''

    # split to paragraph
    t_p = t.split('\n')

    for pNum in range(0, len(t_p)):
        # clear value in variable
        word_p = []
        reordered = []
        reordered_text = ''

        # split to word
        word = t_p[pNum].split()

        # split to char
        for char in word:

            # reverse the word, save into list
            reordered.append(list(char)[::-1])

        # reorder to paragraph
        for r_word in reordered:
            for r_char in r_word:
                reordered_text += r_char
            reordered_text += ' '
        reordered_p.append(reordered_text)

    #Print all paragraph
    for all, p in enumerate(reordered_p):
        reordered_all += reordered_p[all] + '\n'
    return reordered_all

#######
#Result
if __name__ == "__main__":
    print('Example Task:' + str(hammer_pickOneMemeber()))
    print('\n Task 1:' + taskOne())
    # print('Task 2:' + taskTwo())
    print('\n Task 3:' + taskThree())
    print('\n Task 4:' + taskFour(ftext))

    # Task-1 - count the total number of words in the prargraph that contains vowel characters(a, e, i, o u)

    # Task-2 - encode the paragraph by shifting the position of each character by a variable value e.g. I am a boy (1) -> J bn b cpz

    # Task-3 - Reverse the entire paragraph line by line e.g. I am a boy -> yob a ma I
    
    # Task-4 - Reverse the order of character of each word e.g. I am a boy -> I ma a yob
