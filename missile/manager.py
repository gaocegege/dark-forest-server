__author__ = 'gaoce'

from flask import jsonify
from missile import Missile
import json

class Manager:
    def __init__(self):
        self.missileList = []
        self.userPointer = {}

    def toJsonArray(self, pointer):
        ret = []
        for i in range(pointer, len(self.missileList)):
            ret.append(self.missileList[i].toJson())
            print ret
        return json.dumps(ret)

    def push(self, missile):
        self.missileList.append(missile)

    def getMissileList(self, clientId):
        if clientId in self.userPointer:
            ret = self.toJsonArray(self.userPointer[clientId])
            self.userPointer[clientId] = len(self.missileList)
            return ret
        else:
            ret = self.toJsonArray(0)
            self.userPointer[clientId] = len(self.missileList)
            return ret