import perlin
from random import choice, randint

import chunk

from generation.biome import getBiome
from generation.biometypes import Biomes
from generation.noiseSettingsBiome import Settings
from generation.blocksplotch import generatePatchOfStone


from shared import Blocks
from chunk import CHUNK_HEIGHT

noise = perlin.SimplexNoise()
noise.randomize()

POND_GENERATION_HEIGHT_MAXIMUM = CHUNK_HEIGHT/4
POND_GENERATION_HEIGHT_MINIMUM = POND_GENERATION_HEIGHT_MAXIMUM - 5

class WorldGen:
    def generate(world, seed):
        for x in range(2):
            for z in range(2):
                chunk_position = (x - 1, -1, z - 1)
                current_chunk = chunk.Chunk(world, chunk_position)
                
                _ch_x, _ch_y, _ch_z = current_chunk.position
                
                print(f"Chunk generating, [\n absolute = ({_ch_x}, {_ch_z}) \nrelative to loop = ({x}, {z}) \n]")
                
                
                

                for Z in range(_ch_z, _ch_z + chunk.CHUNK_WIDTH):
                    for Y in range(chunk.CHUNK_HEIGHT):
                        for X in range(_ch_x, _ch_x + chunk.CHUNK_LENGTH):
                            biome = getBiome(X, Z)
                            
                            nX = noise.noise3(X/Settings[biome]["scale"], Z/Settings[biome]["scale"], seed)*Settings[biome]["amp"]
                            nY = noise.noise3(Y/Settings[biome]["scale"], X/Settings[biome]["scale"], seed)*Settings[biome]["amp"]
                            nZ = noise.noise3(Z/Settings[biome]["scale"], Y/Settings[biome]["scale"], seed)*Settings[biome]["amp"]
                            
                            density = nX + nY + nZ + X + Y + Z
                            
                            if density < Settings[biome]["maxDensityRequiredToSpawnBlock"] and density > Settings[biome]["leastDensityRequiredToSpawnBlock"]:
                                #print(f"Block placing at ({X}, {Y}, {Z}). Density={density}")
                                WorldGen.placeAppropriateBlock(X, Y, Z, current_chunk, biome)
                            elif density > Settings[biome]["maxDensityRequiredToSpawnBlock"]:
                                if Y >= POND_GENERATION_HEIGHT_MINIMUM and Y <= POND_GENERATION_HEIGHT_MAXIMUM:
                                    current_chunk.blocks[X][Y][Z] = Blocks.WATER
                                    if Y-1 <= POND_GENERATION_HEIGHT_MINIMUM:
                                        current_chunk.blocks[X][Y-1][Z] = Blocks.SAND
                            
                                    

                world.chunks[chunk_position] = current_chunk
        
        for chunk_position in world.chunks:
            world.chunks[chunk_position].update_subchunk_meshes()
            world.chunks[chunk_position].update_mesh()
            
    def placeAppropriateBlock(X, Y, Z, current_chunk, biome):
        if Y == POND_GENERATION_HEIGHT_MAXIMUM+1 or Y == POND_GENERATION_HEIGHT_MAXIMUM+2:
            current_chunk.blocks[X][Y][Z] = Blocks.SAND
        else:
            current_chunk.blocks[X][Y][Z] = Settings[biome]["blocksBelowAir"]
        
            if WorldGen.blockAbove(X, Y, Z, current_chunk):
                if Settings[biome]["generatePatchesOfStone"]:
                    if generatePatchOfStone(X, Z):
                        #print("[WorldGen] Generating block splotch.")
                        current_chunk.blocks[X][Y][Z] = Blocks.STONE
                    else:
                        current_chunk.blocks[X][Y][Z] = Settings[biome]["blocksBelowBlock"]
        
            ### DECORATION LOGIC
            if 'decorations' in Settings[biome] and not WorldGen.outOfRange(Y+1):
                chosenDecoration = choice(
                    Settings[biome]["decorations"]
                )
            
                if chosenDecoration == Blocks.CACTUS:
                    for cactusLength in range(randint(1, 8)):
                        if WorldGen.outOfRange(Y): break
                        if not WorldGen.blockBelow(X, Y, Z, current_chunk): return
                        current_chunk.blocks[X][Y+cactusLength][Z] = chosenDecoration
                else:
                    current_chunk.blocks[X][Y+1][Z] = chosenDecoration
            
    def outOfRange(Y):
        return Y >= CHUNK_HEIGHT
    
    def blockAbove(X, Y, Z, current_chunk):
        if not WorldGen.outOfRange(Y): return False
        return current_chunk.blocks[X][Y+1][Z] != Blocks.AIR
    
    def blockBelow(X, Y, Z, current_chunk):
        if not WorldGen.outOfRange(Y): return False
        return current_chunk.blocks[X][Y-1][Z] != Blocks.AIR