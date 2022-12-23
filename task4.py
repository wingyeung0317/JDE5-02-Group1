# Import Text
text = './news.txt'
f = open(text, "r")
ftext = f.read()
print(ftext + '\n')

# Task 4 (Reverse the order of character of each word e.g. I am a boy -> I ma a yob)
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

#Result of task 4 ( import news.txt to function (task Four) )
print(taskFour(ftext))
