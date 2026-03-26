# minecraft_python_test.py
from mcpi.minecraft import Minecraft
from mcpi import block
import time

# Connect to Minecraft
mc = Minecraft.create()

# Post a message to the chat
mc.postToChat("Hello from Python test!")

# Get player's position
pos = mc.player.getTilePos()

# Place a block under the player
mc.setBlock(pos.x, pos.y - 1, pos.z, block.DIAMOND_BLOCK)

# Build a simple tower of 5 blocks
for i in range(5):
    mc.setBlock(pos.x + 1, pos.y + i, pos.z, block.STONE)
    time.sleep(0.2)  # small delay to see block appear

mc.postToChat("Tower complete!")
