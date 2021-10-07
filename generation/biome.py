import perlin
from generation.biometypes import Biomes

import random
from sys import maxsize

NOISE_OBJ = perlin.SimplexNoise()
NOISE_OBJ.randomize()

SEED = random.randint(-maxsize, maxsize)

SCALE = 35
AMP = 30

SCALE_TEMPERATURE = SCALE-random.randint(3, 15)
AMP_TEMPERATURE = AMP-random.randint(3, 15)

SCALE_HUMIDITY = (SCALE_TEMPERATURE + SCALE)
AMP_HUMIDITY = (AMP + AMP_TEMPERATURE)

def getBiome(X, Z):
    n = NOISE_OBJ.noise3(X/SCALE, Z/SCALE, SEED)*AMP
    
    temperature = NOISE_OBJ.noise3(Z/SCALE_TEMPERATURE, X/SCALE_TEMPERATURE, SEED)*AMP_TEMPERATURE
    humidity = NOISE_OBJ.noise3(X/SCALE_HUMIDITY, Z/SCALE_HUMIDITY, SEED)*AMP_HUMIDITY
    
    n += (temperature + humidity)
    
    if n > -50 and n < -10:
        ### PLAINS
        return Biomes.DESERT
    elif n > -10 and n <= 30:
        ### DESERT
        return Biomes.PLAINS
    elif n > 30:
        return Biomes.SNOWY_MOUNTAINS
    elif n < -50:
        return Biomes.STONEY_MOUNTAINS
    else: 
        ### ERROR
        print(f"[Warning] Unable to find biome, defaulting to plains biome. ({n})")
        return Biomes.PLAINS