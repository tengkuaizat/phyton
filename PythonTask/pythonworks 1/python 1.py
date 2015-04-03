# My 1st chatbox
# blablabla
# filtered = input.replace(" ni ", " <beep> ")
#import BeautifulSoup
import urllib
import urllib2

file = open("stop-words.txt")
stopwords = file.readlines()

#Function section
def stopwordRemover(message):
    for word in stopwords:
        next = word.strip()
        message = message.replace(" " + next + " ", " ")
        next = next.title()
        message = message.replace(" " + next + " ", " ")
    return message

def remove_html_markup(s):
    tag = False
    quote = False
    out = ""

    for c in s:
            if c == '<' and not quote:
                tag = True
            elif c == '>' and not quote:
                tag = False
            elif (c == '"' or c == "'") and tag:
                quote = not quote
            elif not tag:
                out = out + c
    return out


#Starting of Loop
while True:
    #Question 1
    inputtext = raw_input("ELIZA : Hi, What is your name? ")
    inputtext = " " + inputtext + " "
    varname = stopwordRemover(inputtext)
    varname = varname.replace("name","")
    print("Your filtered text was: " + varname.strip())

    #Question 2
    age = raw_input("ELIZA: How old are you " + varname.strip() + "?")
    age = " " + age + " "
    filtered = stopwordRemover(age)
    filtered = filtered.replace("age","")
    filtered = filtered.replace("old","")
    filtered = filtered.strip()
    young = 20
    print("Your age is: " + filtered)
    if int(filtered) <= young:
        print ("Hello young boy!")
    elif int(filtered) > young:
        print ("Hi, you're an adult! Such WOW!")

    #Question 3
    input = raw_input("ELIZA: How is the weather today? ")
    filtered = stopwordRemover(input)
    filtered = filtered.replace("the","")
    filtered = filtered.replace("weather","")
    filtered = filtered.replace("is","")
    varWeather = filtered
    if varWeather == 'sunny':
        print ("I love " + filtered.strip() +" day")
    elif varWeather == 'cold':
        print ("I love " + filtered.strip() +" day")
    elif varWeather == 'cloudy':
        print ("I love " + filtered.strip() +" day")
    else:
        print ("Lovely weather")

    #Question 4
    #opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    input = raw_input("ELIZA: What you want to know today" + varname + "?")
    searchword = input
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = urllib2.Request('http://en.wikipedia.org/wiki/' + searchword.strip(),headers=hdr)
    response = urllib2.urlopen(req)
    the_page = response.read()
    the_page = the_page[the_page.index('<p>'):the_page.index('</p>')]
    the_pagestring = remove_html_markup(the_page)
    print(the_pagestring.strip())
    #------beautifulsoup----------
    #soup = BeautifulSoup(response)
    #theptag = soup.find('<p>')
    #print(theptag.string)
    

    #Question 5 (Random Facts)
    #http://en.wikipedia.org/wiki/Special:Random
