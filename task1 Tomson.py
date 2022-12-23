import random

# Task-1 - count the total number of words in the prargraph that contains vowel characters(a, e, i, o u)
text =str( './news.txt')
f = open(text, "r")
tot = 0
vowels = ['a','e','i','o','u']

for char in f.read():
    if char in vowels:
        tot = tot +1
f.close()

print("\nTotal Vowels are:")
print(tot)

# print(f.read())




# def hammer_pickOneMemeber():
#     '''example function'''

#     teamJDE = ['hammer', 'billy', 'chistina']
#     result = random.sample(teamJDE, 1)
#     return result


# if __name__ == "__main__":
#     print(hammer_pickOneMemeber())
    #  print(taskOne())
    # print(taskTwo())
    # print(taskThree())
    # print(taskFour())

    # Task-1 - count the total number of words in the prargraph that contains vowel characters(a, e, i, o u)