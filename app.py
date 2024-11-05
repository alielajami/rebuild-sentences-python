''' Rebuilding Sentences from a list of words '''
n1 = int(input("Enter the number of words: ")) # Number of words in the sentence
words_list = [] # List to store the words
for i in range(n1): # Loop to get the words from the user
    word = input(f"Enter word {i+1}: ")
    words_list.append(word) # Append the words to the list

numbers_list = [] # List to store the number of letters in each word
for j in range(len(words_list)): # Loop to get the number of letters in each word
    num = int(input(f"Enter the number of letters in word {j+1}: "))
    numbers_list.append(num) # Append the number of letters to the list

def rebuild_sentence(words_array, numbers_array):
    '''' Function to rebuild the sentence from the list of words '''
    modified_words_list = [] # List to store the modified words
    for k in range(len(words_array)): # Loop to modify the words
        modified_word = words_array[k][:numbers_array[k]] # Modify the words
        modified_words_list.append(modified_word) # Append the modified words to the list

    result_sentence = ' '.join(modified_words_list) # Join the modified words to form the sentence
    return result_sentence # Return the sentence

print("Reconstructed sentence:", rebuild_sentence(words_list, numbers_list))
