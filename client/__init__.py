"""
Client class.


"""
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

from world import WorldGen

class Client:
    def __init__(self):
        self.controller = FirstPersonController()
        self.ursina_app = Ursina()
        self.worldgen = WorldGen()
        
    def run(self):
        self.worldgen.generate()
        self.ursina_app.run()
        
if __name__ == "__main__":
    client = Client()
    client.run()
