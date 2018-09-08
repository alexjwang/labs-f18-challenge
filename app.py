from flask import Flask, render_template
import json, requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/pokemon/<query>', methods=['GET'])
def renderPokemon(query):
    URL = 'http://pokeapi.co/api/v2/pokemon/' + query
    r = requests.get(URL)
    data = r.json()

    query2 = query+''

    if query2.isdigit():
        return 'The Pokemon with id ' + query2 + ' is ' + data['name']
    else:
        return query2 + ' has id ' + str(data['id'])


if __name__ == '__main__':
    app.run()
