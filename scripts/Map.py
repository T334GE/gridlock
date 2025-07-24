from scripts.Tile import Tile
from array import array

class Map:
    def __init__(self, width:int, height:int, tiles:list=None):
        """Initialize a map with its width and height."""
        self.__width = width
        self.__height = height
        self.__tiles = tiles if tiles is not None else []

    @property
    def width(self) -> int:
        return self.__width
    @width.setter
    def width(self, value:int):
        if isinstance(value, int):
            self.__width = value
        else:
            raise Exception("Width must be an integer.")

    @property
    def height(self) -> int:
        return self.__height
    @height.setter
    def height(self, value:int):
        if isinstance(value, int):
            self.__height = value
        else:
            raise Exception("Height must be an integer.")

    @property
    def tiles(self) -> list:
        """Return the tiles in the map."""
        return self.__tiles
    @tiles.setter
    def tiles(self, value:list[Tile]):
        """Set the tiles in the map."""
        if isinstance(value, list):
            self.__tiles = value
        else:
            raise Exception("Tiles must be a list of Tile objects.")










if __name__ == "__main__":
    # Example usage
    game_map = Map(10, 10)
