from flask import Flask, redirect, render_template, Blueprint, send_file, url_for, request
from flask_bootstrap import Bootstrap
import random
import googletrans.constants as gc

#this is where the magic happens, pretty much organises the data to be served for each 'route'
main_blueprint = Blueprint('language', __name__)

#display all languages (the request get search doesn't work yet)
@main_blueprint.route('/learn', methods = ['get'])
def main():
    text = request.args.get('jsdata')
    langs = gc.LANGUAGES
    sugg_list = []
    if text:
        sugg_list = {'en':'english'}#[i for i in langs if text.lower() in langs[i]]
    else:
        sugg_list = langs
    for key in sugg_list:
        sugg_list[key] = sugg_list[key].capitalize()
    return render_template('learn.html', languages=langs)


#create a route to handle ajax/jquery requests, for dynamic data retrieval without triggering a page reload
#why is it so slow though?
num = 0
@main_blueprint.route('/getQuestion/<qnum>/<id>', methods=['get'])
def getQuestion(qnum, id):
    #We need to get a question and make it a nice lil json package
    from . import language as lg
    import json
    lesson = lg.gen_lesson(0) #lesson 0
    phrase = lesson["phrases"][int(qnum)]
    translated, pronunciation = lg.translate(phrase, 'en', id)
    wordbank = lg.gen_wordbank(phrase, lesson)
    question = dict()
    question["source"] = phrase
    question["dest"]= translated
    question['pronun'] = pronunciation * (pronunciation != phrase)
    question['wordbank'] = wordbank
    question['length'] = len(lesson['phrases'])
    lg.gen_voice(question["dest"], id)
    return(json.dumps(question))
    
@main_blueprint.route('/learn/<id>', methods = ["get", "post"])
def learn(id):
   return render_template("basegame.html",id=id)
