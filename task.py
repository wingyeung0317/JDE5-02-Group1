import random

text = './news.txt'
f = open(text, "r")
print(f.read())

#hammer
def hammer_pickOneMemeber():
    '''example function'''

    teamJDE = ['hammer', 'billy', 'chistina']
    result = random.sample(teamJDE, 1)
    return result

#Task Three
def taskThree():
    text = './news.txt'
    f = open(text, "r")
    return(f.read()[::-1])

#Task Four
def taskFour(t):
    # Set up variable
    ftext = f.read()
    word_p = []
    reordered = []
    reordered_p = []
    reordered_text = ''

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
        print(reordered_p[all])

#-----
# RUN
if __name__ == "__main__":
    print(hammer_pickOneMemeber())
    # print(taskOne())
    # print(taskTwo())
    print(taskThree())
    print(taskFour(ftext))

    # Task-1 - count the total number of words in the prargraph that contains vowel characters(a, e, i, o u)

    # Task-2 - encode the paragraph by shifting the position of each character by a variable value e.g. I am a boy (1) -> J bn b cpz

    # Task-3 - Reverse the entire paragraph line by line e.g. I am a boy -> yob a ma I
    
    # Task-4 - Reverse the order of character of each word e.g. I am a boy -> I ma a yob
