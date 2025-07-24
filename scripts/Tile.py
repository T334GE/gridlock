class Tile:
    def __init__(self, x:int, y:int):
        """Initialize a tile with its map, position and size."""
        self.__x = x
        self.__y = y
        self.__pos:tuple[int,int] = (x,y)
        self.__contents:list = []

    @property
    def x(self) -> int:
        """Return the x-coordinate of the tile."""
        return self.__x
    @x.setter
    def x(self, value):
        """Set the x-coordinate of the tile."""
        if isinstance(value, int):
            self.__x = value
        else:
            raise ValueError("Y-coordinate must be an integer.")

    @property
    def y(self) -> int:
        """Return the y-coordinate of the tile."""
        return self.__y
    @y.setter
    def y(self, value):
        """Set the y-coordinate of the tile."""
        if isinstance(value, int):
            self.__y = value
        else:
            raise ValueError("Y-coordinate must be an integer.")

    @property
    def pos(self) -> tuple[int,int]:
        return self.__pos
    @pos.setter
    def pos(self, new_pos:tuple[int,int]):
        if not isinstance(new_pos, tuple):
            raise TypeError("new_pos must be a tuple.")
        else:
            self.__pos = new_pos

    @property
    def contents(self) -> list:
        return self.__contents
    @contents.setter
    def contents(self, content):
        if not content:
            raise TypeError("content must be something.")
        else:
            self.__contents.append(content)


    def __repr__(self):
        """Return a string representation of the tile."""
        return f"Tile(\nPosition={self.__pos}\nContents={self.__contents})\n"