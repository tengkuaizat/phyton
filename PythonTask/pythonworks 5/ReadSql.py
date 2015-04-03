import sqlite3

path = "/Users/tmtengkuazmi/Library/Application Support/Google/Chrome/Default/History"
console = sqlite3.connect(path)
cursor = console.cursor()

cursor.execute("SELECT url, title, visit_count, hidden FROM urls WHERE hidden=1 ")

rows = cursor.fetchall()

for row in rows: print row
console.close()
