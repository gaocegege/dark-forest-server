__author__ = 'gaoce'

from flask import jsonify
from missile import Missile
from missile import Player
import json

def dist(player, missile):
    return Math.sqrt(Math.sqr(player.x - missile.x), Math.sqr(player.y - missile.y))

class Manager:
    def __init__(self):
        self.missileList = []
        self.playerList = []

    def update(self, time_span):
        for elem in self.missileList:
            elem.x += elem.vx;
            elem.y += elem.vy;
        
        for missile in self.missileList:
            for player in self.playerList:
                if dist(player, missile) < radius:
                    player.alive = False

    def toJsonArray(self, pointer):
        ret = []
        for i in range(pointer, len(self.missileList)):
            ret.append(self.missileList[i].toJson())
            print ret
        return json.dumps(ret)

    def player_add(self):
        self.playerList.append(Player())
        return len(self.playerList), self.playerList[-1].x, self.playerList[-1].y

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
