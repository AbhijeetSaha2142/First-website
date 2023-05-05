#!/usr/bin/python3

import cgi
import itertools

def htmlTop(): # top of the html, default
    print ('''Content-type:text/html\n\n
    <!DOCTYPE html>

<html lang="en-US">
<!--This is default layout portion. Includes header and sidebar-->
<head>
    <title>Abhijeet Saha's Website</title>
    <link rel="stylesheet" type="text/css" href='style.css'>
    <style>
    h3 {color: white; background-color: powderblue;  font-family: "Times New Roman", Times, serif; font-size: 250%;}
    </style>
</head>
<body>
    <div class="navbar">
        Welcome to Abhijeet Saha's Website
    </div>
    <div class="sidenav">
        <a href="index.html">Home</a>
        <a href="Magic8.html">Magic 8 Ball</a>
        <a href="Anagram.html">Permutation and Anagram Identifier</a>
        <a href="FormResponse.html">Form Response</a>
        <a href="Dictionaries.html">Dictionaries</a>
    </div>
<!--ends here-->''')

def htmlTail(): # bottom of the html, default
    print ('''</body>
        </html>''')

def getdata(): # obtains data from user and returns it
    fieldData = cgi.FieldStorage()
    word = fieldData.getvalue("word")
    return word.lower()

dictionary = open('words.txt', 'r', encoding = 'utf-8') # opens up word dictionary for reading

words = []

for line in dictionary:
    words.append(line.strip()) # adds the words to a list of words

def uniquify(L): # gets rid of duplicate elements in a list
    unique = []
    for i in L:
        if i not in unique:
            unique.append(i)
    return unique
    
def permute(word): # returns all unique permutations of a word
    arrangements = []
    for x in itertools.permutations(word):
        arrangements.append(''.join(x))
    return uniquify(arrangements)

def anagram(L): # returns all anagrams of a something given all its permutaions in a list
    anagrams = []
    for i in L:
        for j in words:
            if i == j:
                anagrams.append(i)
    return uniquify(anagrams)

def main(): # creates the html for the site 
    word = getdata()
    htmlTop()
    print("<div class = 'main'>")
    print('<h3>Anagrams:</h3>')
    for j in anagram(permute(word)):
        print(j + "<br>")
    print('<h3>Permutations:</h3>')
    for i in permute(word):
        print(i + "<br>")
    print("</div>")
    htmlTail()
          
if __name__ == '__main__': # runs the main() function
    try:
        main()
    except:
        cgi.print_exception()
