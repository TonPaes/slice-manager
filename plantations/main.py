import bottle
from bottle import route, run, template, get, post, request

from vars import DOMAIN, PORT
import mongo_driver


app = bottle.default_app()

conn = mongo_driver.mongo_conn()

#will list all mongo colums
@get('/api')
def list_docs_api():
    return "Hello, world! (From Full Stack Python)"

@post('/api')
def insert_docs_api():
    return "hey did you try to upload something?"

@get('/web')
def list_docs_web():
    return '''
        <form action="/web" method="post">
            Temperatura: <input name="temperatura" type="text" />
            Umidade: <input name="umidade" type="text" />
            PH: <input name="ph" type="text"/>
            vento <input name="vento" type="text"/>
            <input value="Insert" type="submit" />
        </form>
    '''

@post('/web')
def insert_docs_web():
    data = { 'temperatura': request.forms.get('temperatura'),
            'umidade': request.forms.get('umidade'),
            'ph': request.forms.get('ph'),
            'vento': request.forms.get('vento'),
    }

    mongo_driver.save_data(conn, data)

    return mongo_driver.show_data(conn)

@route('/results')
def show_results():
    return "Here you see the results"


if __name__ == "__main__":
    run(host="0.0.0.0", port=8000, debug=True, reloader=True)



