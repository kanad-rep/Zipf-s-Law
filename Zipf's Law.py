import matplotlib.pyplot as plt
import string
import math
#from nltk.corpus import stopwords
from collections import Counter

f = open(r"E:\Work\3rd Sem\Information Retrieval\Assignments\Assignment 1\Alice in Wonderland.txt", "r", encoding = 'utf8')
#f = open(r"E:\Work\3rd Sem\Information Retrieval\Assignments\Assignment 1\Sherlock Holmes.txt", "r", encoding = 'utf8')
#f = open(r"E:\Work\3rd Sem\Information Retrieval\Assignments\Assignment 1\The Time Machine.txt", "r", encoding = 'utf8')
l1 = [line for line in f.readlines() if line.strip()]
l2 = []
for line in l1:
    words = line.split(" ")
#    words = line.split("  ")
    for j in words:
        l2.append(j.lower())

f.close()
#Removing punctuations and stopwords
        
def punc(text):
    exclude = set(string.punctuation)
    text = [''.join(x for x in y if x not in exclude) for y in text]
    text = [''.join(x.split()) for x in text]
    text = [x for x in text if x != '']
    return text

l2 = punc(l2)

#Term frequency
tf = Counter(l2)
values = [k for k,l in sorted([(j,i) for i,j in tf.items()], reverse=True)]
log_values = [math.log(k) for k,l in sorted([(j,i) for i,j in tf.items()], reverse = True)]
x = [i+1 for i in range(len(values))]
#plotting,
fig = plt.figure(figsize= (10,8))

plt.subplot(2,1,1)
plt.plot(x,values, 'o')
plt.xlabel('Rank')
plt.ylabel('Frequency')

plt.subplot(2,1,2)
plt.plot(x, log_values, 'o' )
plt.xlabel('Rank')
plt.ylabel('Log(Frequency)')

plt.title("Application of Zipf's Law for the text 'Alice in Wonderland'")