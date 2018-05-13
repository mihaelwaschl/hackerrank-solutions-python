from collections import OrderedDict

word_dictionary = OrderedDict()
num_word = int(input())
count = 1

for i in range(num_word):
    word = input()
    if word in word_dictionary:
        word_dictionary[word] += 1
    else:
        word_dictionary[word] = count
        number_dif_words = len(word_dictionary)
print(number_dif_words)
for j in word_dictionary.values():
    print(j, end=' ')
