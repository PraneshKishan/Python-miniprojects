#This program is for finding the index position of the wordd in input sentence

inp = "Follow pranesh online to learn coding" 
word = 'Pranesh'
final_inp = inp.lower()
final_word = word.lower()

cons = 0

for i in range(len(final_inp)):
    if ord(final_word[cons]) == ord(final_inp[i]):
        print('target index: ',i,"letters: ",inp[i])
        cons+=1
        if cons == len(final_word):
            cons = 0
            continue
