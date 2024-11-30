import random
from utils.grid.grid import Grid

class Wfc:
    def __init__(self, grid: Grid) -> None:
        self.tiles = []
        self.collapsed_tiles = []
        self.grid = grid
        self.tiles_to_check = []
        self.last_collapsed = None

    def get_lowest_entropy_tile(self):
        tile = None
        current_lowest_entropy = 10000
        for row in range(self.grid.num_rows):
            for col in range(self.grid.num_cols):
                entropy = len(self.grid.get_value((row, col)))
                if entropy == 0:
                    continue
                if entropy == 1:
                    tile = (row, col)
                    return tile
                if entropy < current_lowest_entropy:
                    tile = (row, col)
        return tile

    def collapse(self, tile):
        sockets = self.grid.get_value(tile)
        if len(sockets) > 1:
            socket = random.choice(sockets)
        else:
            socket = sockets[0]
        self.grid.set_value(tile, [socket])
        self.collapsed_tiles.append(tile)
        return tile

    def get_neighbors(self, tile):
        # If we are on the top row
        if (tile[0] - 1) < 0:
            n = []
        else:
            n = (tile[0] - 1, tile[1])
        # If we are on the right-most column
        if (tile[1] + 1) == self.grid.num_rows:
            e = []
        else:
            e = (tile[0], tile[1] + 1)
        # If we are on the bottom row
        if (tile[0] + 1) < 0:
            s = []
        else:
            s = (tile[0] + 1, tile[1])
        # If we are on the left-most column
        if (tile[1] - 1) == self.grid.num_cols:
            w = []
        else:
            w = (tile[0], tile[1] - 1) 
        return [n, e, s, w]
        
    def check_tile(self, origin_tile, neighbor_tile, dir: int):
        neighbor_sockets = self.grid.get_value(neighbor_tile)
        if not neighbor_sockets:
            return
        sockets_to_match = [socket[dir] for socket in self.grid.get_value(origin_tile)]
        new_neighbor_sockets = []
        changed = False
        for socket in neighbor_sockets:
            # if the south socket of the north neighbor does not match the north socket of the origin tile.
            if socket[(dir%3)] not in sockets_to_match:
                changed = True
            else:
                new_neighbor_sockets.append(socket)
        if changed:
            self.tiles_to_check.append(neighbor_tile)
        self.grid.set_value(neighbor_tile, new_neighbor_sockets)

    def check_neighbors(self, tile):
        #TODO: replace this code with the check tile func
        changed_tiles = []
        
        neighbor_tiles = self.get_neighbors(tile)
        
        n_sockets = self.grid.get_value(neighbor_tiles[0])
        e_sockets = self.grid.get_value(neighbor_tiles[1])
        s_sockets = self.grid.get_value(neighbor_tiles[2])
        w_sockets = self.grid.get_value(neighbor_tiles[3])
        
        # North
        # Get the north socket of the origin tile.
        if n_sockets:
            sockets_to_match = [socket[0] for socket in self.grid.get_value(tile)]
            new_n_sockets = []
            changed = False
            for socket in n_sockets:
                # if the south socket of the north neighbor does not match the north socket of the origin tile.
                if socket[2] not in sockets_to_match:
                    changed = True
                else:
                    new_n_sockets.append(socket)
            if changed:
                changed_tiles.append(neighbor_tiles[0])
            self.grid.set_value(neighbor_tiles[0], new_n_sockets)

        #East
        if e_sockets:
            sockets_to_match = [socket[1] for socket in self.grid.get_value(tile)]
            new_e_sockets = []
            changed = False
            for socket in e_sockets:
                if socket[3] not in sockets_to_match:
                    changed = True
                else:
                    new_e_sockets.append(socket)
            if changed:
                changed_tiles.append(neighbor_tiles[1])
            self.grid.set_value(neighbor_tiles[1], new_e_sockets)

        #South
        if s_sockets:
            sockets_to_match = [socket[2] for socket in self.grid.get_value(tile)]
            new_s_sockets = []
            changed = False
            for socket in s_sockets:
                if socket[0] not in sockets_to_match:
                    changed = True
                else:
                    new_s_sockets.append(socket)
            if changed:
                changed_tiles.append(neighbor_tiles[2])
            self.grid.set_value(neighbor_tiles[2], new_s_sockets)

        #West
        if w_sockets:
            sockets_to_match = [socket[3] for socket in self.grid.get_value(tile)]
            new_w_sockets = []
            changed = False
            for socket in w_sockets:
                if socket[1] not in sockets_to_match:
                    changed = True
                else:
                    new_w_sockets.append(socket)
            if changed:
                changed_tiles.append(neighbor_tiles[3])
            self.grid.set_value(neighbor_tiles[3], new_w_sockets)
        return changed_tiles

    def propagate(self, origin_tile):
        self.tiles_to_check.extend(self.check_neighbors(origin_tile))
        # look through tile to check and if we change something, add the neighbors of that tile to tile to check. make sure to remove tile to check when done checking.
        while self.tiles_to_check:
            tile = self.tiles_to_check[0]
            self.tiles_to_check.extend(self.check_neighbors(tile))
            self.tiles_to_check.pop(0)

    def advance(self):
        #TODO: Handle getting the image and returning it here so i dont need
        # to awkardly store it.
        tile_to_collapse = self.get_lowest_entropy_tile()
        collapsed_tile = self.collapse(tile_to_collapse)
        self.last_collapsed = (collapsed_tile, self.grid.get_value(collapsed_tile)[0])
        self.propagate(collapsed_tile)
        self.grid.set_value(collapsed_tile, [])
