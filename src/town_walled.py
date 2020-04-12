import sys

import mcpi.block
import mcpi.minecraft


from mcpython.town_wall import TownWall
from mcpython.town import Town

BUILDER_NAME = "ElasticExplorer"

MC_SEVER_HOST = "localhost"
MC_SEVER_PORT = 4711


def main():
    try:
        mc = mcpi.minecraft.Minecraft.create(address=MC_SEVER_HOST, port=MC_SEVER_PORT)

        mc.postToChat("Construyendo una aldea con muralla")
        pos = mc.entity.getTilePos(mc.getPlayerEntityId(BUILDER_NAME))
        pos.x += 10

        wall_thick = 1

        town = Town(mcpi.block.BEDROCK, pos, mc)
        town.build()
        # Position the wall to round the town
        pos.x += wall_thick + town.space + town.house_length
        pos.z -= (town.space + wall_thick)
        town_wall = TownWall(mcpi.block.BRICK_BLOCK, pos, mc)
        town_wall.town = town
        town_wall.thick = wall_thick
        town_wall.build()

    except mcpi.connection.RequestError:
        print("Can't connect to Minecraft server " + MC_SEVER_HOST)


if __name__ == "__main__":
    main()
    sys.exit(0)
