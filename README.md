# upe-hangman

words.txt containing 40k words with alpha letter 
first read the txt into a list
then everytime received a response, the targets will be updated.
Go through all the word in the list and if the length of the string occurs in targets, then check
if the word matches the possible pattern. If so, increase the probability of the characters in the word by 1.

The python file will run the game 101 times and call reset, so probably take a long time considering there is 1 second waiting time between every post guess.

