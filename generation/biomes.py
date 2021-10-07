from generation.biometypes import Biomes

class Biome:
    def __init__(self, name=Biomes.PLAINS, spawnNoiseLeast=0.0, spawnNoiseMaximum=0.0):
        self.spawnNoiseMax = spawnNoiseMaximum
        self.spawnNoiseLow = spawnNoiseLeast