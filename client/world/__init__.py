from ursina import *
from random import randint as rand
from sys import maxsize

class WorldGen:
    def __init__(self,seed=rand(-maxsize, maxsize)):
        self.seed = seed
        
    def generate(self):
        return Entity(model = "cube", scale = (100, 1, 100), collider="box", color=rgb(0, 255, 0))
