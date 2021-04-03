from itertools import permutations
import enchant
import sys
import load_dictionary

word_list = load_dictionary.load('Dictionary_file.txt')

#dictionary=enchant.Dict("en_US") #this imports the US dictionary from the enchant library which is a flat file. Enchant also has the ability to add a pwl or personal word list here
#anagram=set()

anagram_list = []

input_arg=str(sys.argv[1:])
input_arg=input_arg.strip("[']")
letter = [element.lower() for element in input_arg]
sorted_letter = sorted(letter)
count = 0

sorted_input = sorted(input_arg)

flag = True

def isIn(word1,word2):
    for letterx in word2: #word2 is sorted input_arg
        for lettery in word1:
            if letterx not in word1: #word1 is sorted dictionary word
                return False
    return True

for indx in range(0,len(sorted_input)):
    for word in word_list: #using word signature, eliminates the need for permutation search, keeping it under O(n!)
        word = word.lower()
        #indx_input = sorted_letter[0:indx]
        #if sorted(word) == indx_input:
        if isIn(sorted(word),sorted_input):
            count = count + 1  #count is off, but from looking at anagram finders on the net, it could be due to differences in the dictionary used

print(count,"results found")

for indx in range(len(sorted_input),0,-1):
    for word in word_list: #using word signature, hypothesis is an increase of time by an order of magnitude.
        word = word.lower()
        #indx_input = sorted_letter[0:indx]
        #if sorted(word) == indx_input:
        if isIn(sorted(word),sorted_input):
            anagram_list.append(word)
            
    print()
    print(indx, "Letter Words")

    
    for element in sorted(anagram_list): #to fix the print so no reprint of previous iterations occur
        if len(element)>indx:
            pass
        else:
            print(element)
    





