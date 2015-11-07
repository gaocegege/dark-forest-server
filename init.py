__author__ = 'gaoce'

from flask import Flask, jsonify, request
from random import randint
import json
from missile import Manager, Missile

app = Flask(__name__)

lowBound = -500
highBound = 500

manager = Manager()

@app.route('/init', methods=['GET'])
def init():
    newItem = {
        'pos': {
            'x': randint(lowBound, highBound),
            'y': randint(lowBound, highBound)
        },
        'id': str(randint(0, 1000))
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
        missle = jsonStr['missile']

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