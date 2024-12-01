#TODO: Support images with same socket, define socket from multiple points on image.
import os
from pathlib import Path
from PIL import Image
import random
from utils.grid.grid import Grid

class Wfc:
    def __init__(self, grid: Grid, imgs_path) -> None:
        self.tiles = []
        self.collapsed_tiles = []
        self.grid = grid
        self.tiles_to_check = []
        self.is_collapsed = False
        self.imgs_path = Path(imgs_path)
        self.sockets_to_img = {} 
        self.next_img_to_tile = None
        self.parse_images()
        self.rotate_images()
        #print('sockets: -------------------------------------')
        #print(list(self.sockets_to_img.keys()))
        for row in range(self.grid.num_rows):
            for col in range(self.grid.num_cols):
                self.grid.set_value((row, col), list(self.sockets_to_img.keys()))

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
        if not tile:
            self.is_collapsed = True
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
            # if the neighbors opposite socket does not match. 
            socket_dir = socket[-1]
            socket = list(socket[:-1])
            if socket[((dir+2)%4)] not in sockets_to_match:
                changed = True
            else:
                socket.append(socket_dir)
                new_neighbor_sockets.append(socket)
        if changed:
            self.tiles_to_check.append(neighbor_tile)
        #print(f"settin tile {neighbor_tile}, to {new_neighbor_sockets}.")
        self.grid.set_value(neighbor_tile, new_neighbor_sockets)

    def check_neighbors(self, tile):
        #print(f"Checking neighbors of {tile}...")
        neighbor_tiles = self.get_neighbors(tile)
        for i, n_tile in enumerate(neighbor_tiles):
            if not n_tile:
                continue
            if n_tile[1] > self.grid.num_cols or n_tile[1] < 0:
                continue
            #print(f"checking tile: {n_tile}")
            self.check_tile(tile, n_tile, i)

    def propagate(self, origin_tile):
        self.check_neighbors(origin_tile)
        # look through tile to check and if we change something, add the neighbors of that tile to tile to check. make sure to remove tile to check when done checking.
        while self.tiles_to_check:
            tile = self.tiles_to_check[0]
            self.check_neighbors(tile)
            self.tiles_to_check.pop(0)

    def advance(self):
        #TODO: Handle getting the image and returning it here so i dont need
        # to awkardly store it.
        #print("\nadvancing...\n")
        tile_to_collapse = self.get_lowest_entropy_tile()
        #print(f"collaping tile {tile_to_collapse} of value {self.grid.get_value(tile_to_collapse)}.")
        if self.is_collapsed:
            return
        collapsed_tile = self.collapse(tile_to_collapse)
        #print(f"Collapsed tile {collapsed_tile} to value {self.grid.get_value(collapsed_tile)}")
        ##print(self.sockets_to_img)
        self.next_img_to_tile = (self.sockets_to_img[tuple(self.grid.get_value(collapsed_tile)[0])], collapsed_tile, self.grid.get_value(collapsed_tile)[0][-1])
        self.propagate(collapsed_tile)
        self.grid.set_value(collapsed_tile, [])

# IMG PARSING ------------------------------------------------------------

    def parse_images(self):
        img_paths = (self.imgs_path.iterdir())
        rgb_to_socket = {}
        for img_path in img_paths:
            img_sockets = []
            img = Image.open(img_path)
            pixels = img.load()
            
            # North socket
            width, height = img.size
            r, g, b, _ = pixels[width/2, 0]
            socket = None
            if (r, g, b) in rgb_to_socket.keys():
                socket = rgb_to_socket[(r, g, b)]
            else:
                socket = len(rgb_to_socket)
                rgb_to_socket[(r, g, b)] = socket
            img_sockets.append(socket)

            # east socket
            r, g, b, _ = pixels[width-1, height/2]
            socket = None
            if (r, g, b) in rgb_to_socket.keys():
                socket = rgb_to_socket[(r, g, b)]
            else:
                socket = len(rgb_to_socket)
                rgb_to_socket[(r, g, b)] = socket
            img_sockets.append(socket)


            r, g, b, _ = pixels[width/2, height-1]
            socket = None
            if (r, g, b) in rgb_to_socket.keys():
                socket = rgb_to_socket[(r, g, b)]
            else:
                socket = len(rgb_to_socket)
                rgb_to_socket[(r, g, b)] = socket
            img_sockets.append(socket)

            r, g, b, _ = pixels[0, height/2]
            socket = None
            if (r, g, b) in rgb_to_socket.keys():
                socket = rgb_to_socket[(r, g, b)]
            else:
                socket = len(rgb_to_socket)
                rgb_to_socket[(r, g, b)] = socket
            img_sockets.append(socket)

            img_sockets.append(0)
            self.sockets_to_img[tuple(img_sockets)] = img_path

    def rotate_images(self):
        # rotate multiple times
        items_to_add = {}
        for item in self.sockets_to_img.items():
            for rot in range(3):
                sockets = list(item)[0]
                sockets = list(sockets)
                sockets = sockets[:-1]
                print(rot)
                rotated_sockets = sockets[-(rot+1):] + sockets[:-(rot+1)] 
                rotated_sockets.append(rot + 1)
                items_to_add[tuple(rotated_sockets)] = item[1]
        self.sockets_to_img.update(items_to_add)
        for item in self.sockets_to_img.items():
            print(item)