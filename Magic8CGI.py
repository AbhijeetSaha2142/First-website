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
    Question = formData.getvalue("question")
    return Question

def main(): # creates the html for the site
    htmlTop()
    print("<div class = 'main'>")
    print('<p id="A">{}</p>'.format(getdata()))
    print('<p id= "B">And the Omniscient 8 ball answers with<p>')
    print('<p id="A">' + random.choice(["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.",
           "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.",
           "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.",
           "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.",
           "My sources say no.", "Outlook not so good.", "Very doubtful."]) + "</p>")
    print("<br>")
    print('<img src="Ross8ball.jpg" alt="Ross holding an 8 ball" style="float:left; padding: 0  15px 0 0;" width="300",  hspace: 10>')
    print("</div>")
    htmlTail()


if __name__ == '__main__': # runs the main() function
    try:
        main()
    except:
        cgi.print_exception()
