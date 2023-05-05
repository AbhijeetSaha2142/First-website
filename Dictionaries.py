#!/usr/bin/python3

import cgi
import random

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
    formData = cgi.FieldStorage()
    Name = formData.getvalue("name")
    return Name.title()

dictionary = {}

file = open("Pokemon.csv","r", encoding = 'utf-8') # opens file for reading

PokeData = [] # list for storing all the pokemons' data
pokemon = [] # empty list to be used to temporarily store a pokemon's data

for line in file: 
    pokemon = (line.strip()).split(",") # splits the line into a list of the person's data
    PokeData.append(pokemon) # adds in the person's data as a list
PokeData = PokeData[1:] #cuts off first line

file.close() # closes file

PokeDict = {} # dictionary for pokemon

for i in range(len(PokeData)): # makes dictionary of pokemon with names as keys, and stat values
    PokeDict[PokeData[i][1]] = [PokeData[i][0]] + PokeData[i][2:]


def main(): # creates the html for the site
    htmlTop()
    Pokemon = getdata()
    image = (3 - len(PokeDict[Pokemon][0])) * "0" + PokeDict[Pokemon][0] + Pokemon + '.png"'
    print("<div class = 'main'>")
    print('<img src="/~asaha10/Pokemon/' + image + ' alt="Pokemon image" style="float:left; padding: 0  15px 0 0;" width="450",  hspace: 10>')
    print('<p>' + Pokemon + '</p>')
    print('<p>Pokedex number: {}</p>'.format(PokeDict[Pokemon][0]))
    print('<p>Type 1: {}</p>'.format(PokeDict[Pokemon][1]))
    print('<p>Type 2: {}</p>'.format(PokeDict[Pokemon][2]))
    print('<p>Stat Total: {}</p>'.format(PokeDict[Pokemon][3]))
    print('<p>HP: {}</p>'.format(PokeDict[Pokemon][4]))
    print('<p>Attack: {}</p>'.format(PokeDict[Pokemon][5]))
    print('<p>Defense: {}</p>'.format(PokeDict[Pokemon][6]))
    print('<p>Sp. Atk: {}</p>'.format(PokeDict[Pokemon][7]))
    print('<p>Sp. Def: {}</p>'.format(PokeDict[Pokemon][8]))
    print('<p>Speed: {}</p>'.format(PokeDict[Pokemon][9]))
    print('<p>Generation: {}</p>'.format(PokeDict[Pokemon][10]))
    Legendary  = "Nope"
    if PokeDict[Pokemon][11] == "True":
        Legendary = "Yes"
    print('<p>Legendary: {}</p>'.format(Legendary))
    print("</div>")
    htmlTail()


if __name__ == '__main__': # runs the main()
    try:
        main()
    except:
        cgi.print_exception()
