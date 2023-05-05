#!/usr/bin/python3

import cgi

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

def main(): # creates the html for the site
    formData = cgi.FieldStorage()
    title = formData.getvalue("title")
    Name = formData.getvalue("Name")
    item1 = formData.getvalue("item1")
    item2 = formData.getvalue("item2")
    htmlTop()
    print("<div class = 'main'>")
    print('''<p>Dear {title} {Name},<br>
          We have detected someone who has opened a {item1}
          and it's causing the space time continuum to implode. If we all work 
          together we may be able to stop him before the universe reaches critical mass. 
          We need all of you to send us all of your {item2} <br>
          Sincerely, <br>
          The Association of Intergalactic Safety</p>'''.format(title = title, Name = Name, item1 = item1, item2 = item2))
    print("</div>")
    htmlTail()


if __name__ == '__main__': # runs the main() function
    try:
        main()
    except:
        cgi.print_exception()
