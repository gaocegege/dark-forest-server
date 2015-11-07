__author__ = 'gaoce'

import json

class Missile:
    def __init__(self, user_id, x, y, vx, vy):
        self.user_id = user_id;
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def toJson(self):
        return json.dumps({
            'pos': {
                'x': self.x,
                'y': self.y
            },
            'vel': {
                'x': self.vx,
                'y': self.vy
            }
        })
