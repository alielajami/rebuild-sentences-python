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

def rebuild_sentence(words_array, numbers_array):
    '''' Function to rebuild the sentence from the list of words '''
    modified_words_list = []
    for k in range(len(words_array)):
        modified_word = words_array[k][:numbers_array[k]]
        modified_words_list.append(modified_word)

    result_sentence = ' '.join(modified_words_list)
    return result_sentence

print("Reconstructed sentence:", rebuild_sentence(words_list, numbers_list))
