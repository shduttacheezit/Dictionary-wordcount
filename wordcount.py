# put your code here.

import sys 
with open(sys.argv[1], "r") as f: 
    contents = f.read()
# print contents


# def get_word_count(file_name):
#     path = open(file_name)
word_count = {}
words = [word.lower().replace(",", "").replace(".", "").replace("?", "") for word in contents.split()]
print words


# something1 = [word for word in line.lower().split()]
# something2 = [line for line in contents]
# print something1
# print something2
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
for word,number in word_count.iteritems():
    print "{} {}".format(word, number)


# get_word_count("test.txt")