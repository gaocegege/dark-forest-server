__author__ = 'gaoce'

from flask import Flask, jsonify, request
import json
from missile import Manager, Missile

app = Flask(__name__)

manager = Manager()

@app.route('/init', methods=['GET'])
def init():
    cid, x, y = manager.playeradd();
    newItem = {
        'pos': {
            'x': x,
            'y': y
        },
        'id': cid
    }
    return jsonify(newItem)

@app.route('/poll', methods=['POST'])
def poll():
    if "application/json" in request.headers["Content-Type"]:
        cid = request.json['id']
        print 'Manager: ' + manager.missileList.__str__()
        return manager.getMissileList(cid)
    else:
        jsonify({
            'ok': False
        })

@app.route('/event', methods=['POST'])
def event():
    if request.headers['Content-Type'] == 'application/json':
        jsonStr = json.loads(request.data)
        id = jsonStr['id']
        action = jsonStr['action']

        if action == "launch_missle":
            missle = jsonStr['param']
            manager.push(Missile(missle['pos']['x'], \
                                missle['pos']['y'],\
                                missle['vel']['x'],\
                                missle['vel']['y']))
            return jsonify({
               'ok': True
            })
    else:
        print "fxxk"

if __name__ == "__main__":
    app.run(debug=True)
