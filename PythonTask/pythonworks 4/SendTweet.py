import twitter, datetime, time
import urllib, urllib2

while True:
    #Open and read CurrentSession file
    currentSession = open("C:\Users\Prontera\AppData\Local\Google\Chrome\User Data\Default\Current Session", "r")
    #currentSession = open("/Users/farasuhaili/Library/Application Support/Google/Chrome/Default/Current Session", "r")
    lastSession = currentSession.read()
    #---------------------------------


    #Twitter ID and API set
    user = 16907427
    file = open("apitwitter.txt")
    cred = file.readline().strip().split(',')
    api = twitter.Api(consumer_key=cred[0],consumer_secret=cred[1],access_token_key=cred[2],access_token_secret=cred[3])
    #----------------------


    #Check currentsession and find latest URL
    startIndex = lastSession.rfind("http")
    print(startIndex)
    endIndex = lastSession.find(chr(0), startIndex)
    print(endIndex)
    url = lastSession[startIndex:endIndex]
    print(url)
    #----------------------------------------

    #Trying to find title
    response = urllib2.urlopen(url)
    the_page = response.read()
    theTitle = the_page[the_page.index('<title'):the_page.index('</title>')]
    theTitle = theTitle.replace('<title>','')
    print("The title is : " + theTitle.strip())
    #--------------------

    #Send Tweet to Twitter Account
    #timestamp = datetime.datetime.utcnow()
    #response = api.PostUpdate("Tweeted at " + str(timestamp))
    response2 = api.PostUpdate("[PythonProject] I'm really liking " + theTitle.strip() + " at " + url)
    print("Twitter Status Updated!")
    statuses = api.GetUserTimeline(user)
    print("Your latest Twitter status is : " + statuses[0].text)
    #print("Status updated to: " + response.text)
    time.sleep(3600)
    #-----------------------------
    

#Another way to pull the Title from CurrentSession
#(only work with Twitter webpage)
#-------------------------------------------------
#startTitle = lastSession.rfind("title")
#print(startTitle)
#startTitle = startTitle + 9
#endTitle = lastSession.find(chr(0), startTitle)
#print(endTitle)
#webTitle = lastSession[startTitle:endTitle]
#print(webTitle)

#startTitletest = lastSession.find(str(startIndex))
#titleTest = lastSession[startTitletest:20]
#print("test = " + titleTest)
#--------------------------------------------------
