
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
from string import punctuation


#list_of_stopword_extra = ['the', 'a']
stopwords = set(stopwords.words('english')+list(punctuation))
#stopwords here contain high-frequency daily words in ourlife, such as I, am, are, do, and the like,
#these words should not be considered as the keywords, neither should punctuation.

#print(stopwords)

def byFreq(pair):
    return pair[1]  # to return the tuple with the position index = 1

def word_score():
    t = input('which file?')
    raw_text = open(t,'r',encoding='ISO-8859-1').read()
    text = raw_text.lower() #to make all the words in files lowerclass
    for ch in '!"\'#$%&()\'*+,-./:;<=>?@[\\]^_`{|}~': # to get rid of punctuations
        text = text.replace(ch, ' ')
    words = text.split()
    print('Originally there are {} words in the text'.format(len(words)))
    new_list=[x for x in words if x not in stopwords]
    #for w in words:
        #if w in stopwords:
            #print(words)
            #words.remove(w)
            #print(words)
    #if 'the' in new:
        #print('error')

    print('After removing stopwords,{} words are left'.format(len(new_list)))



    counts = defaultdict(int)
    #print(new_list)

    for w in new_list:
        counts[w] += 1

    items = list(counts.items())
    #items.sort()
    items.sort(key = byFreq, reverse = True)
    #print(items[:5])

    print('There are {} distinct words'.format(len(items)))
    distinct_words = int(len(items))
    sentences = sent_tokenize(raw_text)

    word_in_sentence =[word_tokenize(s) for s in sentences]

    list_word_value=[]
    for i in range(len(items)):
        single_word, frequency = items[i]
        single_word, important_value = items[i][0], frequency/len(new_list)
        list_word_value.append((single_word,important_value))

    dict_of_word_value = dict(list_word_value)
    #print(dict_of_word_value.get('FIRST'))

    sentences_value = 0


    single_sentence_value = []
    for i in range(len(sentences)):
        for word in word_in_sentence[i]:
            if word.lower() in new_list:
                word=word.lower()
                sentences_value = float(sentences_value) + dict_of_word_value.get(word)
        # multiple the real value by 10000 for future calculation
                #calculation of sentence value is wrong, reconsider it.
                print(i+1,sentences_value/items[i][1]*10000)


    #print(sentences[1],word_in_sentence[1][1])















word_score()
