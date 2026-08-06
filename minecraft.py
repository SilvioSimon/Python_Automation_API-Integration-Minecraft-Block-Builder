# Import Minecraft API
from mcpi.minecraft import Minecraft
from mcpi import block

# Connect to the running Minecraft instance
mc = Minecraft.create()

# Get current player position
position = mc.player.getTilePos()

# Place a diamond block above the player
mc.setBlock(
    position.x,
    position.y + 1,
    position.z,
    block.DIAMOND_BLOCK.id
)

# Build a 5x5x5 stone cube automatically
for x in range(position.x, position.x + 5):
    for y in range(position.y, position.y + 5):
        for z in range(position.z, position.z + 5):
            mc.setBlock(x, y, z, block.STONE.id)

# Send completion message to Minecraft chat
mc.postToChat("Automation finished: Stone cube created!")
