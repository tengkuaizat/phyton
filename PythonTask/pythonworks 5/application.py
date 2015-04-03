import twitter
import datetime
import re
import urllib2
import sqlite3
from bs4 import BeautifulSoup
from random import randint

file = open('auth.txt')
keys = file.readline().strip().split(',')

path = "/Users/tmtengkuazmi/Library/Application Support/Google/Chrome/Default/History"
console = sqlite3.connect(path)
cursor = console.cursor()

cursor.execute("SELECT url, title, visit_count, hidden FROM urls ORDER BY visit_count DESC LIMIT 1")

#### pick random url WITH title
# cursor.execute("SELECT url, title, visit_count, hidden FROM urls")
# n = 999999
# while True:
#     n = randint(0, len(rows)-1)
#     print n
#     if rows[n][1].strip() != "":
#         break
# print '|' + rows[n][1] + '|'

rows = cursor.fetchall()[0]
title = rows[1].strip()
nView = rows[2]
print title
print nView
console.close()

api = twitter.Api(consumer_key=keys[0], consumer_secret=keys[1], access_token_key=keys[2], access_token_secret=keys[3])

response = api.PostUpdate("I visited " + title + " " + str(nView) + " times in #Chrome #pythonbot #wearecoming")

print("Status posted:s " + response.text)
