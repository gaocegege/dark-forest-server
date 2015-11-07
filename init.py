__author__ = 'gaoce'

from flask import Flask, jsonify, request
import json
import time
from missile import Manager, Missile

app = Flask(__name__)

manager = Manager(time.time())

def update():
    cur_time = time.time()
    manager.update(cur_time - manager.time)
    manager.time = cur_time

@app.route('/init', methods=['GET'])
def init():
    update()
    cid, x, y = manager.playerAdd()
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
    update()
    if "application/json" in request.headers["Content-Type"]:
        cid = request.json['id']
        print 'Manager: ' + manager.missileList.__str__()
        return manager.getMissileList(cid)
    else:
        return jsonify({
            'ok': False
        })

@app.route('/event', methods=['POST'])
def event():
    update()
    if request.headers['Content-Type'] == 'application/json':
        jsonStr = json.loads(request.data)
        id = jsonStr['id']
        action = jsonStr['action']

        if action == "launch_missile":
            missle = jsonStr['param']
            manager.push(Missile(id, \
                                missle['pos']['x'], \
                                missle['pos']['y'],\
                                missle['vel']['x'],\
                                missle['vel']['y']))
            return jsonify({
                'ok': True
            })
        else:
            return jsonify({
                'ok': False
            })
    else:
        return jsonify({
            'ok': False
        })

if __name__ == "__main__":
    app.run(host='0.0.0.0')
