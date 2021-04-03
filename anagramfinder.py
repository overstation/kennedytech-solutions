from itertools import permutations
import enchant
import sys



def sigcheck(word1, word2):
	if sorted(word1) == sorted(word2):
		return True
	else:
		return False
	

dictionary=enchant.Dict("en_US") #this imports the US dictionary from the enchant library which is a flat file. Enchant also has the ability to add a pwl or personal word list here
anagram=set()

input_arg=input("Enter a word: ")



letter = [element.lower() for element in input_arg]
count = 0

for indx in range(1,len(input_arg)):
    for indy in list(permutations(letter,indx)): #permutation from length to position in
        word="".join(indy)
        if dictionary.check(word):
            if indx==1:
                pass
            else:
                count = count + 1  #count is off, but from looking at anagram finders on the net, it could be due to differences in the dictionary used

print(count,"results found")

for indx in range(len(input_arg),1,-1):
    for indy in list(permutations(letter,indx)): #this is recursive, any word longer than 10 characters will take an unknown, LONG period of time to execute.  10 letters took 5-10 minutes, 9 took just over a minute.
        word="".join(indy)
        if dictionary.check(word):
            anagram.add(word)
            
    print()
    print(indx, "Letter Words")

    
    for element in sorted(anagram): #to fix the print so no reprint of previous iterations occur
        if len(element)>indx:
            pass
        else:
            print(element)
    





