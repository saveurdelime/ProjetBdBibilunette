
from flask import Flask, render_template, request
from json import loads
import requests

app = Flask(__name__)
@app.route('/')
def acceuil():
    return render_template('bibilnpageacceuil.html')

@app.route('/bibilnapropos/')
def bibilnapropos():
    return render_template('bibilnapropos.html')

@app.route('/bibilncatalogue/')
def bibilncatalogue():
    return render_template('bibilncatalogue.html')

@app.route('/bibilnlunettespourlui/')
def bibilnlunettespourlui():
    return render_template('bibilnlunettespourlui.html')

@app.route('/bibilnlunettespourelle/')
def bibilnlunettespourelle():
    return render_template('bibilnlunettespourelle.html')

@app.route('/bibilnsinscrire/')
def bibilnsinscrire():
    return render_template('bibilnsinscrire.html')


# <div class = "barredenavigation">
# <a href="/bibilnpageaccueil">Accueil</a>
# <a href="/bibilncatalogue">Catalogue</a>
# <a href="/bibilnlunettespourlui">Lunettes pour lui</a>
# <a href="/bibilnlunettespourelle">Lunettes pour elle</a>
# <a href="/bibilnapropos">À propos</a>
# <a class="liensespaceclient" href="/bibilnseconnecter">Se connecter</a>
# <a class="liensespaceclient" href="/bibilnsinscrire">S'inscrire</a>
# </div>



if __name__=='__main__':
    app.run()
