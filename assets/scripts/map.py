import pytmx

class Map:
    def __init__(self):
        self.__tile_map = pytmx.TiledMap("../sewers.tmx")
        self.__layers = self.__tile_map.visible_layers





if __name__ == "__main__":
    map_instance = Map()
