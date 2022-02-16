from flask import Flask, render_template, Blueprint, send_file, url_for, request
from flask_bootstrap import Bootstrap
import random
import googletrans.constants as gc
main_blueprint = Blueprint('language', __name__)
@main_blueprint.route('/learn', methods = ['get'])
def main():
    text = request.args.get('jsdata')
    langs = gc.LANGUAGES
    sugg_list = []
    if text:
        sugg_list = {'hi':'hindi'}#[i for i in langs if text.lower() in langs[i]]
    else:
        sugg_list = langs
    for key in sugg_list:
        sugg_list[key] = sugg_list[key].capitalize()
    return render_template('learn.html', languages=langs)


currentQuestion = 0
@main_blueprint.route('/learn/<id>', methods = ["get", "post"])
def learn(id):
   global currentQuestion
   from . import language as lg
   
   uput = request.form.get("inputt")

  
   lesson = lg.gen_lesson(0)
   if request.method == 'POST' and uput and uput.replace(' ', '').lower() == lesson["phrases"][currentQuestion].replace(' ', '').lower():
       currentQuestion += 1
   phrase = lesson["phrases"][currentQuestion]
   translated, pronunciation = lg.translate(phrase, 'en', id)
   wordbanks = lg.gen_wordbank(phrase, lesson)
   lesson["phrases"] = phrase
   lesson['translation'] = translated
   lesson['pronunciation'] = pronunciation
   lesson['wordbank'] = wordbanks
   lg.gen_voice(lesson["translation"], id)
   if pronunciation == phrase:
       lesson['pronunciation'] = ''
   return render_template("basegame.html",id=id, lesson=lesson, qnum= currentQuestion)
