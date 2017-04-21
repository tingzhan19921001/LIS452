import string #for using string punctuation
import random
def scrambled_words(s):

    s1 = ''

    for c in string.punctuation:# here string. punctiation refers to '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
        s = s.replace(c,'') ##in this loop, we replace all the punctuation above with none

    l = s.split()
    lcopy = l.copy() #to creat a copy of l
    # we can use random.shuffle. much less work required
    
    #print(l)
    for i in range(len(l)):
        a = random.randint(0,len(lcopy)-1) ##randomly choose a index
        s1 += lcopy[a] + ' ' #add the item using the index
        del lcopy[a] ##delete the one just used to prevent being used another time
    s1 = s1.strip() #stip the final space that is unwanted

    return s1



print(scrambled_words('I do not like green eggs and ham.'))
