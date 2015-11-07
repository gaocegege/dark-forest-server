__author__ = 'gaoce'

from missile import Missile
from manager import Manager

manager = Manager()

manager.push(Missile(1, 2, 3, 4))
manager.push(Missile(1, 2, 3, 4))
manager.push(Missile(1, 2, 3, 4))

print(manager.getMissileList(0))
