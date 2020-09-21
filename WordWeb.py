from flask import Flask, render_template, request, session
from flask_session import Session
import numpy as np
import pandas as pd
import json
import os
from glob import glob
import random


app = Flask(__name__)
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)


@app.route('/')
def startForm():
    session.clear()
    session['nodes'] = []
    session['links'] = []
    session['words'] = []
    return render_template('start-form.html')

@app.route('/', methods=['POST'])
def form_post():
    word = (request.form['word'])
    nodes = setNodes(word)
    links = setLinks(word)
    words = setWords(word)
    return render_template('start-form.html', wordlist=str(words))

@app.route('/wordMap')
def wordMap():
    return render_template('index.html')

def setNodes(word):
    session['nodes'].append({"id": word, "group": 1})
    return session['nodes']

def setLinks(word):
    if (len(session['words']) > 0):
        for element in session['words']:
            ranint = random.randint(0, 1)
            if (ranint == 1):
                session['links'].append({"source": word, "target": element, "value": 1})
    return session['links']

def setWords(word):
    session['words'].append(word)
    return session['words']

@app.route('/getData')
def dataForViz():
    nodes = session['nodes']
    links = session['links']
    data = {
        "nodes": nodes,
        "links": links
    }
    return data