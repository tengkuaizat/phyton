from __future__ import print_statement
import random
from speech import *

CONVERSING = True

memory = []
greetings = ['hola', 'hello', 'hi','hey!','Hello','Hi']
questions = ['How are you?','How are you doing?']
responses = ['Okay','I am fine']
validations = ['yes','yeah','yea','no','No','Nah','nah']
verifications = ['Are you sure?','You sure?','you sure?','sure?',"Sure?"]

engagement_pairs = (greetings, greetings), (questions, responses), (verifications, validations)

while CONVERSING:
    lang = 'en-US'
    speed = .3
    
    userInput = raw_input(">>>Me: ")
    for triggers, outputs in engagement_pairs:
        if not user_input in triggers:
            continue
            
		random_output = random.choice(outputs)
            
        say(random_output, lang, speed)
        print(random_output)
        memory.append((userInput, random_output))
        break
        
    else:
        if 'sure' in userInput:
            response = "Sure about what?"
            say(response,lang,speed)
            memory.append(('sure',response))
            print response
        else:
            say("I did not understand what you said. Goodbye",lang,speed)
            CONVERSING = False