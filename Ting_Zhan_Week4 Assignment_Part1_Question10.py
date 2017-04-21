import string
def main():
    sentence = input('Please enter a sentence to find out the average word length:')
    for c in string.punctuation:
        sentence = sentence.replace(c,'') ## to remove all the punctuation
    s = sentence.split()
    print(s)
    n1 = len(s) ## to find out how many words in the sentence
    n2 = len(sentence)-n1+1 ## to find out how many letters in the sentence
    print('The average world length in a sentence is', n2/n1) ## because in the question it does not specify whether i should round the result, therefore i do not. 

main()
