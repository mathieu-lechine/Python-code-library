#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 08:52:38 2018

@author: mathieu.lechine
"""

import re

#Python Regex Cheatsheet
#https://www.debuggex.com/cheatsheet/regex/python

#Official doc
#https://docs.python.org/3/library/re.html

#Official tutorial
#https://docs.python.org/3/howto/regex.html



###################### Compiling Regular Expressions ######################
#saving the resulting regular expression object for reuse is more efficient when the 
#expression will be used several times in a single program.
#use r'' -> Raw string: so r"\n" is a two-character string containing '\' and 'n', while 
#"\n" is a one-character string containing a newline.
p = re.compile(r'ab*', re.IGNORECASE) #Perform case-insensitive matching
p

###################### Performing Matches ######################
#%%
#match() -> Determine if the RE matches at the beginning of the string
#return None if no match can be found. If they’re successful, a match object instance is 
#returned, containing information about the match: where it starts and ends, the substring 
#it matched, and more.

print(p.match("zab"))
p.match("a")
m = p.match("ab")


#search: Scan through a string, looking for any location where this RE matches.
print(p.search("zab"))
p.search("a")
m = p.search("zab")

#Match object instances also have several methods and attributes; the most important 
#ones are: group, start, end, span
m.group()
m.start()
m.end()
m.span()

#example of use:
regex = r"^bla*"
s = "blaaabbd"
p = re.compile(regex)
m = p.match(s)
if m:
    print('Match found: ', m.group())
else:
    print('No match')





#findall: Find all substrings where the RE matches, and returns them as a list.
p = re.compile('\d+')
liste = p.findall('12 drummers drumming, 11 pipers piping, 10 lords a-leaping')
#finditer: Find all substrings where the RE matches, and returns them as an iterator.
iterator = p.finditer('12 drummers drumming, 11 pipers piping, 10 lords a-leaping')
for match in iterator:
    print(match.span())



################### Module level-functions ###################################
#use the flag re.VERBOSE to make regex easier to read by adding comments
charref = re.compile(r"""
 &[#]                # Start of a numeric entity reference
 (
     0[0-7]+         # Octal form
   | [0-9]+          # Decimal form
   | x[0-9a-fA-F]+   # Hexadecimal form
 )
 ;                   # Trailing semicolon
""", re.VERBOSE)
#The re.VERBOSE flag has several effects. Whitespace in the regular expression that isn’t 
#inside a character class is ignored. This means that an expression such as dog | cat is 
#equivalent to the less readable dog|cat, but [a b] will still match the characters 'a', 
#'b', or a space. In addition, you can also put comments inside a RE; comments extend from
# a # character to the next newline. When used with triple-quoted strings, this enables 
#REs to be formatted more neatly:


################### More Pattern Power ###################################
 
##More Metacharacters
#beginning: ^ or \A (different interpretation in multiline mode)
#end: $ or \Z (different interpretation in multiline mode)
#\b: word boundary
#This is a zero-width assertion that matches only at the beginning or end of a word. A 
#word is defined as a sequence of alphanumeric characters, so the end of a word is 
#indicated by whitespace or a non-alphanumeric character.
p = re.compile(r'\bclass\b')
print(p.search('no class at all'))
print(p.search('the declassified algorithm'))
print(p.search('one subclass is'))
#\B: opposite of \b, only matching when the current position is not at a word boundary.
 

#%%
##Grouping
#Groups are marked by the '(', ')' metacharacters. '(' and ')' have much the same meaning 
#as they do in mathematical expressions; they group together the expressions contained 
#inside them, and you can repeat the contents of a group with a repeating qualifier, such 
#as *, +, ?, or {m,n}.

p = re.compile('(ab)*')
print(p.match('ababababab').span())

#Groups are numbered starting with 0. Group 0 is always present; it’s the whole RE, so 
#match object methods all have group 0 as their default argument.
#Subgroups are numbered from left to right, from 1 upward. Groups can be nested; to deter-
#mine the number, just count the opening parenthesis characters, going from left to right.
p = re.compile('(a(b)c)d')
m = p.match('abcd')
m.group(0)
m.group(1)
m.group(2)
m.group(2,1)
m.groups()

#Backreferences in a pattern allow you to specify that the contents of an earlier captu-
#ring group must also be found at the current location in the string. For example, \1 will
#succeed if the exact contents of group 1 can be found at the current position, and fails 
#otherwise. 

#the following RE detects doubled words in a string.
p = re.compile(r'\b(\w+)\s+\1\b') 
#\s :Matches any whitespace character; this is equivalent to the class [ \t\n\r\f\v]
#\w :Matches any alphanumeric character; this is equivalent to the class [a-zA-Z0-9_] 
p.search('Paris in thê thê spring').group(0)


#%%
#Introduction:
#Perl 5 is well known for its powerful additions to standard regular expressions. For 
#these new features the Perl developers couldn’t choose new single-keystroke metacharacters 
#or new special sequences beginning with \ without making Perl’s regular expressions con-
#fusingly different from standard REs. If they chose & as a new metacharacter, for example
#, old expressions would be assuming that & was a regular character and wouldn’t have es-
#caped it by writing \& or [&].

#The solution chosen by the Perl developers was to use (?...) as the extension syntax. ? 
#immediately after a parenthesis was a syntax error because the ? would have nothing to 
#repeat, so this didn’t introduce any compatibility problems. The characters immediately 
#after the ? indicate what extension is being used, so (?=foo) is one thing (a positive 
#lookahead assertion) and (?:foo) is something else (a non-capturing group containing the 
#subexpression foo).

#Python supports several of Perl’s extensions and adds an extension syntax to Perl’s 
#extension syntax. If the first character after the question mark is a P, you know that 
#it’s an extension that’s specific to Python.



##Non-capturing (?:...) and Named Groups (?P<name>...)

#Sometimes you’ll want to use a group to denote a part of a regular expression, but 
#aren’t interested in retrieving the group’s contents. You can make this fact explicit by
# using a non-capturing group: (?:...)
m = re.match("(?:[abc])+", "abc")
m.groups()

#A more significant feature is named groups: instead of referring to them by numbers, 
#groups can be referenced by a name. 
#The syntax for a named group is one of the Python-specific extensions: (?P<name>...).


InternalDate = re.compile(r'INTERNALDATE "'
        r'(?P<day>[ 123][0-9])-(?P<mon>[A-Z][a-z][a-z])-'
        r'(?P<year>[0-9][0-9][0-9][0-9])'
        r' (?P<hour>[0-9][0-9]):(?P<min>[0-9][0-9]):(?P<sec>[0-9][0-9])'
        r' (?P<zonen>[-+])(?P<zoneh>[0-9][0-9])(?P<zonem>[0-9][0-9])'
        r'"')

##Lookahead Assertions (?=...)  -> negative: (?!...)
#Positive lookahead assertion. This succeeds if the contained regular expression, repre- 
#sented here by ..., successfully matches at the current location, and fails otherwise. 
#But, once the contained expression has been tried, the matching engine doesn’t advance at
#all; the rest of the pattern is tried right where the assertion started.

#example of use: exclude files with bat and exe extension
p = re.compile(r""".*#Name of the file
               [.]#dot of the file
               (?!bat$|exe$)[^.]*$""", re.VERBOSE) 
p.match("filename.exe.doc.exe")


#%%
################### Modifying strings ###################################

##Splitting Strings: split
p = re.compile(r'\W+')
p.split('This is a test, short and sweet, of split().')
p.split('This is a test, short and sweet, of split().', maxsplit=3)
#to know the delimiters
p2 = re.compile(r'(\W+)')
p2.split('This... is a test.')

##Search and Replace: sub and subn
#Another common task is to find all the matches for a pattern, and replace them with a 
#different string. The sub() method takes a replacement value, which can be either a 
#string or a function, and the string to be processed.
p = re.compile('(blue|white|red)')
p.sub('Hé', 'blue socks and red shoes')
p.subn('Hé', 'blue socks and red shoes')

#replacement with groups
p = re.compile('section{ (?P<name> [^}]* ) }', re.VERBOSE)
p.sub(r'subsection{\1}','section{First} section{second}')
p.sub(r'subsection{\g<name>}','section{First} section{second}')

#replcement with function
#the replacement function translates decimals into hexadecimal:
def hexrepl(match):
    "Return the hex string for a decimal number"
    value = int(match.group())
    return hex(value)

p = re.compile(r'\d+')
p.subn(hexrepl, 'Call 65490 for printing, 49152 for user code.')

#using non-greedy match: ?
s = '<html><head><title>Title</title>'
print(re.match('<.*>', s).group())
print(re.match('<.*?>', s).group())

