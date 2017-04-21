def main():
    phrase = input('Please enter a phrase, to get the acronym for the phrase.')
    acronym = ''
    wordlist= phrase.split()
    for word in wordlist:
        acronym = acronym + word[0] #to get the first letter of each word and join them
    print('Your acronym is,',acronym.upper())
    
main()
