# Import Minecraft API
from mcpi.minecraft import Minecraft
from mcpi import block
import time

# Connect to the running Minecraft game
mc = Minecraft.create()

# Get the player's position
pos = mc.player.getTilePos()

# Place a block above the player (e.g., diamond block)
mc.setBlock(pos.x, pos.y + 1, pos.z, block.DIAMOND_BLOCK.id)

# Build a cube of stone blocks
for x in range(pos.x, pos.x + 5):
    for y in range(pos.y, pos.y + 5):
        for z in range(pos.z, pos.z + 5):
            mc.setBlock(x, y, z, block.STONE.id)