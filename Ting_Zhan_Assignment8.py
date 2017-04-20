from collections import defaultdict

#import os
#os.chdir('/Users/zhanting/Documents/coursework/LIS452/weely assignment/week8 assignment/')

def byFreq(pair):
    return pair[1]  # to return the tuple with the position index = 1

def wordsort(t):
    # get the sequence of words from the file
    #fname = input("File to analyze: ")
    text = open(t,'r',encoding='ISO-8859-1').read()
    text = text.lower() #to make all the words in files lowerclass
    for ch in '!"\'#$%&()\'*+,-./:;<=>?@[\\]^_`{|}~': # to get rid of punctuations
        text = text.replace(ch, ' ')
    words = text.split()
    return words # return so it can be called outside the function

def countword(t):
    words = wordsort(t) # to get list named words throught function wordsort()
    # construct a dictionary of word counts
    counts = defaultdict(int)  # dict where non-existent keys get automatically assigned an integer 0
    for w in words:
        counts[w] += 1       
    return words, counts # return so it can be called outside the function


def totalword(t):
    t_words = wordsort(t) #to call function wordsort() and assign the result as t_words
    totalword = len(t_words) #find out how many words in total
    print('There are',totalword,'total words in',t)
    # construct a dictionary of word count
    t_words, t_counts = countword(t) #to call function countword() and assign the results to t_word, t_counts

    distinctword = len(list(t_counts.items())) # len() helps us to find out how many items in list named t_counts.items
    print('There are',distinctword,'distinct words')
    
    return totalword, distinctword #return so it can be called outside the function

def minisort(t):
    words, counts = countword(t) #to assign the results as variable words, counts
    tw = len(words) #to get how many total words
    items = list(counts.items()) # to build a list named items
    items.sort() #to sort alphatically 
    items.sort(key = byFreq, reverse = True) #to sort out by frequency 
    return words, counts, tw, items 

def itemsort(t1,t2):
    
    n = eval(input("For how many words do you want to see results?")) # how many words you want to analyze
    
    print('The most frequent words in data_files/',t1)
    for i in range(n):
        words1, counts1, tw1, items1 = minisort(t1) #assign the results as words1, counts1, tw1, items1
        word1,count1 = items1[i] #to assign the results as word1, count1
        p1 = round(float(count1)/float(tw1)*100,2) #to calculate p1 and round to 2 decimals
        print('{0:<15}{1:>5}'.format(word1,count1),p1,'%')
        
    print('The most frequent words in data_files/',t2)        
    for i in range(n):
        words2, counts2, tw2, items2 = minisort(t2)#assign the results as words2, counts2, tw2, items2
        word2,count2 = items2[i] #to assign the results as word2, count2
        p2 = round(float(count2)/float(tw2)*100,2)#to calculate p2 and round to 2 decimals
        print('{0:<15}{1:>5}'.format(word2,count2),p2,'%')
             
    #print('{0:<15}{1:>5}{0:.2f}%'.format(word,count,p)) #0:.2f  why report error

def word_frequency(t):
    words, counts = countword(t) #assign the results as words,counts
    tw,dw = totalword(t) #assign the results as tw, dw
    items = list(counts.items()) #to build list name items that include element in counts.items 
    items.sort() #to sort out aphalbetically
    for i in range(dw): # dw = len(list(t_counts.items()))
        word,count = items[i] # to assign the results as word, count
        
    return words, counts, word, count,items #words refer to total words list, counts refers to dictionary like the wordfrequency example
    

def main():
    print("This program analyzes two text files to compute the frequency of words,")
    print("and to list repeated words found only in one of the two files.\n")
    t1= input('First file to analyze:')
    t2 = input('Second file to analyze:')
    words1, counts1, word1, count1,items1 = word_frequency(t1) #assign the results to variable words1, counts1, word1, count1,items1  
    words2, counts2, word2, count2,items2 = word_frequency(t2) #assign the results to variable words2, counts2, word2, count2,items2
    itemsort(t1,t2) #to print out the percentage of each selected word
    print('The following words appeared at least twice in data_files/{} but never in data_files/{}'.format(t1,t2))
    wantedwords1=[] #to build a new list first
    for word1, count1 in items1:
        if count1 > 1 and word1 not in words2: # build up conditions that the frequency is larger than 1 and not in list words2
            wantedwords1.append(word1) # to append each word1 to the list wantedwords1
    print(wantedwords1)

    print('The following words appeared at least twice in data_files/{} but never in data_files/{}'.format(t2,t1))
    wantedwords2=[] 
    for word2, count2 in items2:
        if count2 > 1 and word2 not in words1:
            wantedwords2.append(word2) # to append each word2 to the list wantedwords2
    print(wantedwords2)
   

# This "magic" line below will allow this file to be imported by another script
# without automatically executing the functions contained in it:
if __name__ == '__main__':  main()
