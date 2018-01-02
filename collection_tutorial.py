#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 10:39:13 2018

@author: mathieu.lechine
"""
############IMPORT TEXT WITH NLTK######################
from nltk.corpus import gutenberg
from nltk.corpus import stopwords
import string
from nltk.tokenize import RegexpTokenizer

#choose en ebook from Gutenberg project
gutenberg.fileids()
txt_raw = gutenberg.raw('melville-moby_dick.txt')
tokenizer = RegexpTokenizer(r'\w+')
word_list = tokenizer.tokenize(txt_raw)
print("Nombre de mots: {}".format(len(word_list)))
#remove stopwords
word_list = [w.lower() for w in word_list if not w.lower() in stopwords.words('english')]
print("Nombre de mots after stopwords removel: {}".format(len(word_list)))

#%%############# COLLECTIONS COUNTER############################
from collections import Counter
# Tally occurrences of words in a list
word_list_ex = ['red', 'blue', 'red', 'green', 'blue', 'blue']
cnt = Counter()
for word in word_list_ex:
    cnt[word] += 1
cnt
#find the most common words
cnt = Counter(word_list)
n=10
cnt.most_common(n)
cnt.most_common()[:-n-1:-1]
#unique words
dictionnaire = sorted(list(cnt))
print('Nombre de mots différents: {}'.format(len(dictionnaire)))

#%%############# COLLECTIONS deque############################
#Deques are a generalization of stacks and queues (the name is pronounced “deck” 
#and is short for “double-ended queue”). Deques support thread-safe, memory efficient appends 
#and pops from either side of the deque with approximately the same O(1) performance in either direction.
from collections import deque
import itertools
d = deque('athie')
d.append('u')                    # add a new entry to the right side
d.appendleft('M')
print(d)
print(d.pop())
print(d.popleft())
d.extend('-bal') 
d.rotate(1)
print(d)

#exemple of use
filename = "/Users/mathieu.lechine/Dropbox (Optimind Winter)/Python-learning/Python_DataCamp/Data/house-votes-84.names.txt"
def tail(filename, n=10):
    'Return the last n lines of a file'
    return deque(open(filename), maxlen = n)
tail(filename)

def moving_average(iterable, n=3):
    # moving_average([40, 30, 50, 46, 39, 44]) --> 40.0 42.0 45.0 43.0
    # http://en.wikipedia.org/wiki/Moving_average
    it = iter(iterable)
    d = deque(itertools.islice(it, n-1))
    d.appendleft(0)
    s = sum(d)
    for elem in it:
        s += elem - d.popleft()
        d.append(elem)
        yield s / float(n)

iterable = [40, 30, 50, 46, 39, 44]
for i in moving_average(iterable, n=3):
    print(i)

#%%############# COLLECTIONS defaultdict############################
#Returns a new dictionary-like object. defaultdict is a subclass of the built-
#in dict class. It overrides one method and adds one writable instance variable. 
#The remaining functionality is the same as for the dict class and is not documented here.

#The first argument provides the initial value for the default_factory attribute; 
#it defaults to None. All remaining arguments are treated the same as if they were passed 
#to the dict constructor, including keyword arguments.
from collections import defaultdict

#Using list as the default_factory, it is easy to group a sequence of key-value 
#pairs into a dictionary of lists
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)
print(sorted(d.items()))

#Setting the default_factory to int makes the defaultdict useful for counting 
#(like a bag or multiset in other languages)
s = "mississippi"
d = defaultdict(int)
for c in s:
    d[c] += 1
sorted(d.items())


#%%############# COLLECTIONS OrderedDict############################
#Ordered dictionaries are just like regular dictionaries but they remember the 
#order that items were inserted. When iterating over an ordered dictionary, the 
#items are returned in the order their keys were first added.

from collections import OrderedDict

d = OrderedDict.fromkeys('Mathieu')
d.move_to_end('M')
''.join(d.keys())
d.move_to_end('M', last=False)
''.join(d.keys())

#regular unsorted dictionary
d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}

# dictionary sorted by key
OrderedDict(sorted(d.items(), key=lambda t: t[0]))

# dictionary sorted by value
OrderedDict(sorted(d.items(), key=lambda t: t[1]))

# dictionary sorted by length of the key string
OrderedDict(sorted(d.items(), key=lambda t: len(t[0])))

#%%############# COLLECTIONS namedtuple############################
#Named tuples assign meaning to each position in a tuple and allow for more readable, 
#self-documenting code. They can be used wherever regular tuples are used, and they add 
#the ability to access fields by name instead of position index.


from collections import namedtuple

#basic examples
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, y=25)
p.x + p.y
p[0] + p[1]
x, y = p 

#Named tuples are especially useful for assigning field names to result tuples returned 
#by the csv or sqlite3 modules:
filename = "/Users/mathieu.lechine/Dropbox (Optimind Winter)/Python-learning/Input/employees.csv"
EmployeeRecord = namedtuple('EmployeeRecord', 'name, age, title, department, paygrade')
import csv
for emp in map(EmployeeRecord._make, csv.reader(open(filename, "rt"))):
    print(emp.name, emp.title)














