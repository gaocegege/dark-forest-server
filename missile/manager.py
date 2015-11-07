__author__ = 'gaoce'

from flask import jsonify
from missile import Missile
from missile import Player
import json

def dist(player, missile):
    return Math.sqrt(Math.sqr(player.x - missile.x), Math.sqr(player.y - missile.y))

class Manager:
    def __init__(self, time):
        self.missileList = []
        self.playerList = []
        self.time = time

    def time(self):
        return self.time

    def set_time(self, cur_time):
        self.time = cur_time;

    def update(self, time_span):
        for elem in self.missileList:
            elem.x += elem.vx;
            elem.y += elem.vy;
        
        for missile in self.missileList:
            for player in self.playerList:
                if dist(player, missile) < radius:
                    player.alive = False

    def infoToJson(self, clientId):
        ret = []
        for i in range(self.playList[clientId].current_version, len(self.missileList)):
            ret.append(self.missileList[i].toJson())
            print ret
        res = {
                'alive': self.playerList[clientId].alive,
                'missile_list': ret
                }

        return json.dumps(res)

    def player_add(self):
        self.playerList.append(Player())
        return len(self.playerList), self.playerList[-1].x, self.playerList[-1].y

    def push(self, missile):
        self.missileList.append(missile)

    def getMissileList(self, clientId):
        if clientId < len(self.playerList):
            ret = self.infoToJson(clientId)
            self.playerList[clientId].current_version = len(self.missileList)
            return ret
        else:
            return ""
