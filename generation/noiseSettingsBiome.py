from generation.biomes import Biomes
from shared import Blocks

Settings = {
    # Plains Biome
    Biomes.PLAINS: {"scale": 40, "amp": 25, "blocksBelowAir": Blocks.GRASS, 
                    "blocksBelowBlock": Blocks.DIRT, 
                    "decorations": [Blocks.AIR, Blocks.AIR, Blocks.AIR, Blocks.AIR, Blocks.DAISY, Blocks.ROSE, Blocks.ALLIUM, Blocks.LILY_OF_THE_VALLEY], 
                    "generatePatchesOfStone": True, "maxDensityRequiredToSpawnBlock": 20, "leastDensityRequiredToSpawnBlock": 15},
    
    # Taiga Biome
    Biomes.TAIGA: {"scale": 40, "amp": 25, "blocksBelowAir": Blocks.GRASS, 
                   "blocksBelowBlock": Blocks.DIRT, 
                   "decorations": [Blocks.AIR, Blocks.AIR, Blocks.AIR, Blocks.AIR, Blocks.DEAD_BUSH, Blocks.DAISY, Blocks.ALLIUM], 
                   "generatePatchesOfStone": False, "maxDensityRequiredToSpawnBlock": 22, "leastDensityRequiredToSpawnBlock": 10},
    
    # Desert Biome
    Biomes.DESERT: {"scale": 40, "amp": 22, "blocksBelowAir": Blocks.SAND, 
                    "blocksBelowBlock": Blocks.SANDSTONE, 
                    "decorations": [Blocks.AIR, Blocks.AIR, Blocks.AIR, Blocks.AIR, Blocks.DEAD_BUSH, Blocks.CACTUS], 
                    "generatePatchesOfStone": False, "maxDensityRequiredToSpawnBlock": 25, "leastDensityRequiredToSpawnBlock": 5},
    
    # Snowy Mountains Biome
    Biomes.SNOWY_MOUNTAINS: {"scale": 40, "amp": 24, "blocksBelowAir": Blocks.SNOWY_GRASS, 
                             "blocksBelowBlock": Blocks.DIRT, 
                             "decorations": [Blocks.AIR, Blocks.AIR, Blocks.AIR, Blocks.AIR, Blocks.DEAD_BUSH, Blocks.LILY_OF_THE_VALLEY, Blocks.ALLIUM], 
                             "generatePatchesOfStone": True, "maxDensityRequiredToSpawnBlock": 35, "leastDensityRequiredToSpawnBlock": 0},
    
    # Stoney Mountains Biome
    Biomes.STONEY_MOUNTAINS: {"scale": 40, "amp": 25, "blocksBelowAir": Blocks.STONE, 
                              "blocksBelowBlock": Blocks.STONE, 
                              "decorations": [Blocks.AIR, Blocks.AIR, Blocks.AIR, Blocks.AIR], 
                              "generatePatchesOfStone": True, "maxDensityRequiredToSpawnBlock": 22, "leastDensityRequiredToSpawnBlock": 19}
}