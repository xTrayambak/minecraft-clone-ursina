import perlin
import random
import sys

noise = perlin.SimplexNoise()
noise.randomize()

SEED = random.randint(-sys.maxsize, sys.maxsize)

SCALE = 5
AMP = 15

def generatePatchOfStone(X, Z):
    noiseVal = noise.noise3(X/SCALE, Z/SCALE, SEED)*AMP
    if noiseVal > -10 and noiseVal < -7:
        return True
    
    return False