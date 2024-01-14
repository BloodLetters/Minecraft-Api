import asyncio

from waitress import serve
from data import config, query
from flask import Flask, redirect, jsonify

class Api:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.json.sort_keys = False
        self.routes()

    def routes(self):
        self.app.add_url_rule('/api', 'api', self.api)
        self.app.add_url_rule('/', 'index', self.index)
        self.app.register_error_handler(404, self.page_not_found)
    
    def api(self):
        data = asyncio.run(query())
        datas = 0
        
        if data:
            structure = {
                "server_online": True,
                "ip": config()['ip'],
                "port": config()['port'],
                "online": data.players.online,
                "max": data.players.max,
                "players": {},
                "version": data.version.name,
                "protocol": data.version.protocol
                }
            
            for player in data.players.sample:
                datas = datas + 1
                structure["players"][str(datas)] = {
                    "name": player.name,
                    "uuid": player.id
                }
            return jsonify(structure)
        else:
            offline = {
                "isonline": False,
                "ip": config()['ip'],
                "port": config()['port'],
                "online": -1,
                "max": -1,
                "players": {},
                "version": -1,
                "protocol": -1
            }
            return jsonify(offline)
        

    def index(self):
        return '<h1>Halo Dunia</h1>'

    def page_not_found(self, error):
        return redirect('/')

    def run(self):
        self.app.run(debug=True)

if __name__ == '__main__':
    serve(Api().app, host='0.0.0.0', port=5000)