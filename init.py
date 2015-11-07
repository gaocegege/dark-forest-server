__author__ = 'gaoce'

from flask import Flask, jsonify, request
from random import randint
from missile import Manager, Missile

app = Flask(__name__)

lowBound = 0
highBound = 1000

manager = Manager()

@app.route('/init', methods=['GET'])
def init():
    newItem = {
        'pos': {
            'x': randint(lowBound, highBound),
            'y': randint(lowBound, highBound)
        },
        'id': str(randint(lowBound, highBound))
    }
    return jsonify(newItem)

@app.route('/poll', methods=['POST'])
def poll():
    cid = request.json['id']
    return manager.getMissileList(cid)

@app.route('/event', methods=['POST'])
def event():
    id = request.json['id']
    missle = request.json['missile']

    manager.push(Missile(missle['pos']['x'], \
                         missle['pos']['y'],\
                         missle['vel']['x'],\
                         missle['vel']['y']))

if __name__ == "__main__":
    app.run(host='0.0.0.0')