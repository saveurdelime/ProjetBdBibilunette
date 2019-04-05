
from flask import Flask, render_template, request
from json import loads
from infrastructure import BibiRepository

import requests

app = Flask(__name__)
bibi_Repository = BibiRepository()

@app.route('/')
def acc():
    return render_template('bibilnpageacceuil.html')

@app.route('/bibilnpageaccueil/')
def acceuil():
    return render_template('bibilnpageacceuil.html')

@app.route('/bibilnapropos/')
def bibilnapropos():
    return render_template('bibilnapropos.html')

@app.route('/bibilncatalogue/')
def catalogue():
    data=bibi_Repository.get_tableLunette()
    return render_template('bibilncatalogue.html', data=data)




@app.route('/bibilnlunettespourlui/')
def bibilnlunettespourlui():
    return render_template('bibilnlunettespourlui.html')

@app.route('/bibilnlunettespourelle/')
def bibilnlunettespourelle():
    return render_template('bibilnlunettespourelle.html')

@app.route('/bibilnsinscrire/')
def bibilnsinscrire():
    return render_template('bibilnsinscrire.html')

@app.route('/bibilnseconnecter/')
def bibilnseconnecter():
    return render_template('bibilnseconnecter.html')



if __name__=='__main__':
    app.run()
