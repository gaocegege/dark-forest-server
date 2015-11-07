__author__ = 'gaoce'

from flask import jsonify
from missile import Missile
from player import Player
from player import lowBound 
from player import highBound
import json

radius = 4

scale_factor = 10

def dist_sqr(player, missile):
    return (player.x - missile.x) ** 2 + (player.y - missile.y) ** 2

def valid(missile):
    return missile.x >= lowBound and missile.x <= highBound and missile.y <= highBound and missile.y >= lowBound

class Manager:
    def __init__(self, time):
        self.missileList = []
        self.playerList = []
        self.time = time

    def update(self, time_span):
        for elem in self.missileList:
            elem.x += elem.vx * time_span * scale_factor
            elem.y += elem.vy * time_span * scale_factor
        
        self.missileList = [m for m in self.missileList if valid(m)]

        for i in xrange(0, len(self.playerList)):
            if self.playerList[i].alive:
                for missile in self.missileList:
                    if dist_sqr(self.playerList[i], missile) < radius ** 2 and missile.user_id != i:
                        self.playerList[i].alive = False
                        print "{cid} is killed by {killer}".format(cid = i, killer = missile.user_id)

    def infoToJson(self, clientId):
        ret = []
        for i in range(self.playerList[clientId].current_version, len(self.missileList)):
            ret.append(self.missileList[i].toJson(clientId))
            print ret
        res = {
                'alive': self.playerList[clientId].alive,
                'missile_list': ret
                }

        return json.dumps(res)

    def playerAdd(self):
        self.playerList.append(Player())
        cid = len(self.playerList) - 1
        return cid, self.playerList[cid].x, self.playerList[cid].y

    def push(self, missile):
        self.missileList.append(missile)

    def getMissileList(self, clientId):
        if clientId < len(self.playerList):
            ret = self.infoToJson(clientId)
            self.playerList[clientId].current_version = len(self.missileList)
            return ret
        else:
            return '{"ok":false}'
