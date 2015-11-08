__author__ = 'gaoce'

import json

class Missile:
    def __init__(self, user_id, x, y, vx, vy):
        self.user_id = user_id;
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def toJson(self, cid):
        return json.dumps({
            'mine': int(cid == self.user_id),
            'pos_x': self.x,
            'pos_y': self.y,
            'vel_x': self.vx,
            'vel_y': self.vy
        })
