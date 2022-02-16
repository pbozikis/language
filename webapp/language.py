from googletrans import Translator
import json
import random

translator = Translator()
def translate(text, src, dest):
    translation = translator.translate(text, dest = dest, src = src)
    return translation.text, translation.pronunciation
def gen_wordbank(phrase, current_lesson):
    wordBank = phrase.split() + [i for i in current_lesson["phrases"][random.randint(0, len(current_lesson))].split() if i not in phrase]
    random.shuffle(wordBank)
    return wordBank

def gen_lesson(lessonNum):
    f = open("c:/Users/panbo/Desktop/apps/language/webapp/static/phrases.json", "r")
    '''jason = {
     "lessons":[
         {"phrases":["Hello", "How are you?", "My name is Pablo", "What is your name?", "Nice to meet you", "I am good, thank you", "Hello Pablo"]
           
         },
       {"phrases":["Hello", "A man", "A woman", "A dog", "The man and the woman", "You are a woman", "Pablo is a man"]}
     ]}'''
    jason = f.read()
    #current_lesson = json.loads(jason)["lessons"][lessonNum]
    #current_lesson = json.loads(jason)["lessons"][lessonNum]

    return current_lesson


# def flashcard(text):
#     lang, phon = translate(text)
#     ans = input(f"What's {lang}({phon}) mean in English? ")
#     if ans == text:
#         print("Correct! Good work!")
#     else:
#         print("U stipud")
#         print(f"It's actually: {text}")
    
#lesson one
# print("Welcome to this app, you're probably here because you're scared of the duolingo owl...")
# input()
# print("Well you're not safe here, we have Pablo the Frog, and he will kill your entire family if yoy fail this course...")
# input()
# print("Have fun!")