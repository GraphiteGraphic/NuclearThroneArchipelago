import sys
from worlds.nuclear_throne.Client import launch
import Utils
import ModuleUpdate
ModuleUpdate.update()

if __name__ == "__main__":
    Utils.init_logging("NuclearThroneClient", exception_logger="Client")
    launch(*sys.argv[1:])
