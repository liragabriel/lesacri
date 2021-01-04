import json
from lesacri.alcorao import alcorao
from lesacri.biblia import biblia
from lesacri.tora import tora
from flask import Flask


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/alcorao')
@app.route('/alcorao/<sura>')
@app.route('/alcorao/<sura>/<versiculo>')
def get_alcorao(sura=None, versiculo=None):
    response = alcorao(sura, versiculo, debug=True)
    return response

@app.route('/biblia')
@app.route('/biblia/<livro>')
@app.route('/biblia/<livro>/<capitulo>')
@app.route('/biblia/<livro>/<capitulo>/<versiculo>')
def get_biblia(livro=None, capitulo=None, versiculo=None):
    response = biblia(livro, capitulo, versiculo, debug=True)
    return response

@app.route('/tora')
@app.route('/tora/<livro>')
@app.route('/tora/<livro>/<capitulo>')
@app.route('/tora/<livro>/<capitulo>/<versiculo>')
def get_tora(livro=None, capitulo=None, versiculo=None):
    response = tora(livro, capitulo, versiculo, debug=True)
    return response


if __name__ == '__main__':
    app.run(debug=True)
