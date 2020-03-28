import sys

from mcpi import block
from mcpi.minecraft import Minecraft

# El objetivo de este tutorial es construir pirámides en Minecraft

BUILDER_NAME = "ElasticExplorer"

MC_SEVER_HOST = "javierete.com"
MC_SEVER_PORT = 8711
PYRAMID_HEIGHT = 10
PYRAMID_BLOCK = block.SANDSTONE

# Nos conectamos al servidor de Minecraft
mc = Minecraft.create(address=MC_SEVER_HOST, port=MC_SEVER_PORT)
mc.postToChat("¡Construyendo una pirámide de " + str(PYRAMID_HEIGHT) + " de altura!")

# Buscamos la posición en el mundo de nuestro jugador
# Esto sólo vale en singleplayer
# p = mc.player.getTilePos()
p = mc.entity.getTilePos(mc.getPlayerEntityId(BUILDER_NAME))

# La pirámide la hacemos delante del jugador

BUILDER_NAME = "ElasticExplorer"

init_x = p.x + 1
init_y = p.y
init_z = p.z

# La longitud (x) y la anchura (z) siempre son iguales
# La relación entre la altura y la longitud/anchura es Longitud/Anchura = 2 * Altura - 1
length = 2 * PYRAMID_HEIGHT - 1
width = 2 * PYRAMID_HEIGHT - 1

# Dibujamos la pirámide por niveles hasta llegar a 1 bloque en la altura final
for i in range(0, PYRAMID_HEIGHT):
    level = i
    mc.setBlocks(init_x + level,              init_y + level, init_z + level,
                 init_x + (length-1) - level, init_y + level, init_z + (width-1) - level,
                 block.SAND)

# TODO: Movemos al jugador a la cima de la pirámide
sys.exit(0)
