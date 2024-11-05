''' Rebuilding Sentences from a list of words '''
n1 = int(input("Enter the number of words: "))
words_list = []
for i in range(n1):
    word = input(f"Enter word {i+1}: ")
    words_list.append(word)

numbers_list = []
for j in range(len(words_list)):
    num = int(input(f"Enter the number of letters in word {j+1}: "))
    numbers_list.append(num)

print(words_list, numbers_list)
