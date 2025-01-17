import os
from functools import lru_cache

import pygame
import pyganim
import random

from cultivate import settings

# todo: the spritesheets may be loaded from disk multiple tiles


@lru_cache(None)
def get_music(path: str) -> pygame.mixer.Sound:
    path = path.replace("/", os.sep).replace("\\", os.sep)
    path = os.path.join(settings.MUSIC_DIR, path)
    return pygame.mixer.Sound(path)


@lru_cache(None)
def get_sound(path: str) -> pygame.mixer.Sound:
    path = path.replace("/", os.sep).replace("\\", os.sep)
    path = os.path.join(settings.SOUNDS_DIR, path)
    return pygame.mixer.Sound(path)


@lru_cache(None)
def get_font(filename: str, size: int) -> pygame.font.Font:
    path = os.path.join(settings.FONTS_DIR, filename)
    return pygame.font.Font(path, size)

@lru_cache(None)
def get_image(path: str, has_alpha: bool = False) -> pygame.Surface:
    canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
    image = pygame.image.load(canonicalized_path)
    if has_alpha:
        return image.convert_alpha()
    else:
        return image.convert()


@lru_cache(None)
def get_grass(width: int, height: int) -> pygame.Surface:
    # load the grass tile from the sprite sheet
    grass_tile = pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'foliage4.png'),
        rects=[(269, 333, 16, 16)])[0].convert()

    # create a blank surface to paint with grass
    grass = pygame.Surface((width, height), pygame.SRCALPHA, 32).convert_alpha()

    # paint grass tiles onto surface
    for i in range(0, width, 16):
        for j in range(0, height, 16):
            grass.blit(grass_tile, (i, j))
    return grass


@lru_cache(None)
def get_river(height):
    tiles = [
        (64, 48, 16, 16),  # left river
        (80, 48, 16, 16),  # middle river
        (112, 48, 16, 16)  # right river
    ]
    images = pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'river1.png'),
        rects=tiles)
    for image in images:
        image.convert_alpha()
    river = pygame.Surface((128, height), pygame.SRCALPHA, 32).convert_alpha()

    # make left column
    for i in range(0, height, 16):
        river.blit(images[0], (0, i))
        for j in range(0, 96, 16):
            river.blit(images[1], ((16 + j), i))
        river.blit(images[2], (112, i))
    return river


@lru_cache(None)
def get_floor(width: int, height: int) -> pygame.Surface:
    # load the floor tile from the sprite sheet
    floor_tile = pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'floors1.png'),
        rects=[(0, 0, 16, 16)])[0].convert()

    # create a blank surface to tile
    floor = pygame.Surface((width, height), pygame.SRCALPHA, 32).convert()

    # tile the floor
    for i in range(0, height, 16):
        for j in range(0, width, 16):
            floor.blit(floor_tile, (i, j))
    return floor

@lru_cache(None)
def get_character(filename, direction):
    tiles = [
        (3, 130, 25, 36),  # facing forward
        (27, 130, 25, 36),
        (52, 130, 25, 36),
        (3, 166, 24, 34),  # facing backwards
        (27, 166, 26, 36),
        (52, 166, 26, 36),
        (3, 202, 25, 34),  # facing to the right
        (27, 202, 25, 34),
        (52, 202, 25, 34),
        (3, 236, 25, 34),  # facing to the right
        (27, 236, 25, 34),
        (52, 236, 25, 34)
    ]
    char_tiles = pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, filename),
        rects=tiles)
    for tile in char_tiles:
        tile.convert_alpha()
    character = pygame.Surface(
        (23, 34), pygame.SRCALPHA, 32).convert_alpha()

    if direction == 'forward':
        dir_tiles = [
            char_tiles[0],
            char_tiles[1],
            char_tiles[0],
            char_tiles[2]
        ]
    elif direction == 'backward':
        dir_tiles = [
            char_tiles[3],
            char_tiles[4],
            char_tiles[3],
            char_tiles[5]
        ]
    elif direction == 'right':
        dir_tiles = [
            char_tiles[6],
            char_tiles[7],
            char_tiles[6],
            char_tiles[8]
        ]
    elif direction == 'left':
        dir_tiles = [
            char_tiles[9],
            char_tiles[10],
            char_tiles[9],
            char_tiles[11]
        ]
    else:
        dir_tiles = [
            char_tiles[0]
            ]
    frames = list(zip(dir_tiles,
                      [100, 100, 100, 100]))
    animChar = pyganim.PygAnimation(frames)
    animChar.play()

    return animChar

@lru_cache(None)
def get_player(direction=None):
    return get_character("chars1.png", direction)

@lru_cache(None)
def get_npc(direction=None):
    return get_character("chars1-2.png", direction)

@lru_cache(None)
def get_npc2(direction=None):
    tiles = [
        (1, 128, 30, 32), # forward
        (33, 128, 30, 32),
        (66, 128, 30, 32),
        (1, 160, 30, 32), # left
        (33, 160, 30, 32),
        (66, 160, 30, 32),
        (1, 192, 30, 32), # right
        (33, 192, 30, 32),
        (66, 192, 30, 32),
        (0, 224, 30, 32), # backward
        (33, 224, 30, 32),
        (66, 224, 30, 32)
    ]
    char_tiles = pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, "chars5.png"),
        rects=tiles)
    character = pygame.Surface(
        (30, 32), pygame.SRCALPHA, 32).convert_alpha()

    if direction == 'forward':
        dir_tiles = [
            char_tiles[0],
            char_tiles[1],
            char_tiles[0],
            char_tiles[2],
        ]
    elif direction == 'backward':
        dir_tiles = [
            char_tiles[9],
            char_tiles[10],
            char_tiles[9],
            char_tiles[11],
        ]
    elif direction == 'right':
        dir_tiles = [
            char_tiles[6],
            char_tiles[7],
            char_tiles[6],
            char_tiles[8],
        ]
    elif direction == 'left':
        dir_tiles = [
            char_tiles[3],
            char_tiles[4],
            char_tiles[3],
            char_tiles[5],
        ]
    else:
        dir_tiles = [
            char_tiles[0]
            ]
    frames = list(zip(dir_tiles,
                      [200, 200, 200, 200]))
    animChar = pyganim.PygAnimation(frames)
    animChar.play()
    return animChar

@lru_cache(None)
def get_npc5(direction=None):
    tiles = [
        (98, 0, 30, 32), # forward
        (130, 0, 30, 32),
        (161, 0, 30, 32),
        (98, 34, 30, 32), # left
        (130, 34, 30, 32),
        (161, 34, 30, 32),
        (98, 65, 30, 32), # right
        (130, 65, 30, 32),
        (161, 65, 30, 32),
        (98, 98, 30, 32), # right
        (130, 98, 30, 32),
        (161, 98, 30, 32),
    ]
    char_tiles = pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, "chars2.png"),
        rects=tiles)
    character = pygame.Surface(
        (30, 32), pygame.SRCALPHA, 32).convert_alpha()

    if direction == 'forward':
        dir_tiles = [
            char_tiles[0],
            char_tiles[1],
            char_tiles[0],
            char_tiles[2],
        ]
    elif direction == 'backward':
        dir_tiles = [
            char_tiles[9],
            char_tiles[10],
            char_tiles[9],
            char_tiles[11],
        ]
    elif direction == 'right':
        dir_tiles = [
            char_tiles[6],
            char_tiles[7],
            char_tiles[6],
            char_tiles[8],
        ]
    elif direction == 'left':
        dir_tiles = [
            char_tiles[3],
            char_tiles[4],
            char_tiles[3],
            char_tiles[5],
        ]
    else:
        dir_tiles = [
            char_tiles[0]
            ]
    frames = list(zip(dir_tiles,
                      [150, 150, 150, 150]))
    animChar = pyganim.PygAnimation(frames)
    animChar.play()
    return animChar

@lru_cache(None)
def get_npc_innocent(direction=None):
    tiles = [
        (1, 128, 30, 32), # forward
        (33, 128, 30, 32),
        (66, 128, 30, 32),
        (1, 160, 30, 32), # left
        (33, 160, 30, 32),
        (66, 160, 30, 32),
        (1, 192, 30, 32), # right
        (33, 192, 30, 32),
        (66, 192, 30, 32),
        (0, 224, 30, 32), # backward
        (33, 224, 30, 32),
        (66, 224, 30, 32)
    ]
    char_tiles = pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, "chars9.png"),
        rects=tiles)
    character = pygame.Surface(
        (30, 32), pygame.SRCALPHA, 32).convert_alpha()

    if direction == 'forward':
        dir_tiles = [
            char_tiles[0],
            char_tiles[1],
            char_tiles[0],
            char_tiles[2],
        ]
    elif direction == 'backward':
        dir_tiles = [
            char_tiles[9],
            char_tiles[10],
            char_tiles[9],
            char_tiles[11],
        ]
    elif direction == 'right':
        dir_tiles = [
            char_tiles[6],
            char_tiles[7],
            char_tiles[6],
            char_tiles[8],
        ]
    elif direction == 'left':
        dir_tiles = [
            char_tiles[3],
            char_tiles[4],
            char_tiles[3],
            char_tiles[5],
        ]
    else:
        dir_tiles = [
            char_tiles[0]
            ]
    frames = list(zip(dir_tiles,
                      [200, 200, 200, 200]))
    animChar = pyganim.PygAnimation(frames)
    animChar.play()
    return animChar

@lru_cache(None)
def get_npc3(direction=None):
    tiles = [
        (193, 128, 30, 32), # forward
        (225, 128, 30, 32),
        (257, 128, 30, 32),
        (193, 160, 30, 32), # left
        (225, 160, 30, 32),
        (257, 160, 30, 32),
        (193, 192, 30, 32), # right
        (225, 192, 30, 32),
        (257, 192, 30, 32),
        (193, 224, 30, 32), # backward
        (225, 224, 30, 32),
        (257, 224, 30, 32)
    ]
    char_tiles = pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, "chars5.png"),
        rects=tiles)
    character = pygame.Surface(
        (30, 32), pygame.SRCALPHA, 32).convert_alpha()

    if direction == 'forward':
        dir_tiles = [
            char_tiles[0],
            char_tiles[1],
            char_tiles[2]
        ]
    elif direction == 'backward':
        dir_tiles = [
            char_tiles[9],
            char_tiles[10],
            char_tiles[11]
        ]
    elif direction == 'right':
        dir_tiles = [
            char_tiles[6],
            char_tiles[7],
            char_tiles[8]
        ]
    elif direction == 'left':
        dir_tiles = [
            char_tiles[3],
            char_tiles[4],
            char_tiles[5]
        ]
    else:
        dir_tiles = [
            char_tiles[0]
            ]
    frames = list(zip(dir_tiles,
                      [100, 100, 100]))
    animChar = pyganim.PygAnimation(frames)
    animChar.play()
    return animChar

@lru_cache(None)
def get_npc_cat(direction=None):
    tiles = [
        (435, 12, 42, 42),
        (483, 12, 42, 42),
        (530, 12, 42, 42),
        (435, 63, 42, 42),
        (483, 63, 42, 42),
        (530, 63, 42, 42),
        (435, 110, 42, 42),
        (483, 110, 42, 42),
        (530, 110, 42, 42),
        (435, 156, 42, 42),
        (483, 156, 42, 42),
        (530, 156, 42, 42),
    ]
    char_tiles = pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, "cats1.png"),
        rects=tiles)
    character = pygame.Surface(
        (30, 32), pygame.SRCALPHA, 32).convert_alpha()

    if direction == 'forward':
        dir_tiles = [
            char_tiles[0],
            char_tiles[1],
            char_tiles[2]
        ]
    elif direction == 'backward':
        dir_tiles = [
            char_tiles[9],
            char_tiles[10],
            char_tiles[11]
        ]
    elif direction == 'right':
        dir_tiles = [
            char_tiles[6],
            char_tiles[7],
            char_tiles[8]
        ]
    elif direction == 'left':
        dir_tiles = [
            char_tiles[3],
            char_tiles[4],
            char_tiles[5]
        ]
    else:
        dir_tiles = [
            char_tiles[0]
            ]
    frames = list(zip(dir_tiles,
                      [100, 100, 100]))
    animChar = pyganim.PygAnimation(frames)
    animChar.play()
    return animChar

@lru_cache(None)
def get_npc4(direction=None):
    tiles = [
        (99, 2, 27, 31),
        (131, 2, 27, 31),
        (163, 2, 27, 31),
        (99, 34, 27, 31),
        (131, 34, 27, 31),
        (163, 34, 27, 31),
        (99, 66, 27, 31),
        (131, 66, 27, 31),
        (163, 66, 27, 31),
        (99, 98, 27, 31),
        (131, 98, 27, 31),
        (163, 98, 27, 31)
    ]
    char_tiles = pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, "chars6.png"),
        rects=tiles)
    character = pygame.Surface(
        (30, 32), pygame.SRCALPHA, 32).convert_alpha()

    if direction == 'forward':
        dir_tiles = [
            char_tiles[0],
            char_tiles[1],
            char_tiles[2]
        ]
    elif direction == 'backward':
        dir_tiles = [
            char_tiles[9],
            char_tiles[10],
            char_tiles[11]
        ]
    elif direction == 'right':
        dir_tiles = [
            char_tiles[6],
            char_tiles[7],
            char_tiles[8]
        ]
    elif direction == 'left':
        dir_tiles = [
            char_tiles[3],
            char_tiles[4],
            char_tiles[5]
        ]
    else:
        dir_tiles = [
            char_tiles[0]
            ]
    frames = list(zip(dir_tiles,
                      [100, 100, 100]))
    animChar = pyganim.PygAnimation(frames)
    animChar.play()
    return animChar

@lru_cache(None)
def get_npc_white_robes(direction=None):
    tiles = [
        (1, 128, 30, 32), # forward
        (33, 128, 30, 32),
        (66, 128, 30, 32),
        (1, 160, 30, 32), # left
        (33, 160, 30, 32),
        (66, 160, 30, 32),
        (1, 192, 30, 32), # right
        (33, 192, 30, 32),
        (66, 192, 30, 32),
        (0, 224, 30, 32), # backward
        (33, 224, 30, 32),
        (66, 224, 30, 32)
    ]
    char_tiles = pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, "chars10.png"),
        rects=tiles)
    character = pygame.Surface(
        (30, 32), pygame.SRCALPHA, 32).convert_alpha()

    if direction == 'forward':
        dir_tiles = [
            char_tiles[0],
            char_tiles[1],
            char_tiles[0],
            char_tiles[2],
        ]
    elif direction == 'backward':
        dir_tiles = [
            char_tiles[9],
            char_tiles[10],
            char_tiles[9],
            char_tiles[11],
        ]
    elif direction == 'right':
        dir_tiles = [
            char_tiles[6],
            char_tiles[7],
            char_tiles[6],
            char_tiles[8],
        ]
    elif direction == 'left':
        dir_tiles = [
            char_tiles[3],
            char_tiles[4],
            char_tiles[3],
            char_tiles[5],
        ]
    else:
        dir_tiles = [
            char_tiles[0]
            ]
    frames = list(zip(dir_tiles,
                      [150, 150, 150, 150]))
    animChar = pyganim.PygAnimation(frames)
    animChar.play()
    return animChar

@lru_cache(None)
def get_npc_pink_robes(direction=None):
    tiles = [
        (1, 128, 30, 32), # forward
        (33, 128, 30, 32),
        (66, 128, 30, 32),
        (1, 160, 30, 32), # left
        (33, 160, 30, 32),
        (66, 160, 30, 32),
        (1, 192, 30, 32), # right
        (33, 192, 30, 32),
        (66, 192, 30, 32),
        (0, 224, 30, 32), # backward
        (33, 224, 30, 32),
        (66, 224, 30, 32)
    ]
    char_tiles = pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, "pink_chars.png"),
        rects=tiles)
    character = pygame.Surface(
        (30, 32), pygame.SRCALPHA, 32).convert_alpha()

    if direction == 'forward':
        dir_tiles = [
            char_tiles[0],
            char_tiles[1],
            char_tiles[0],
            char_tiles[2],
        ]
    elif direction == 'backward':
        dir_tiles = [
            char_tiles[9],
            char_tiles[10],
            char_tiles[9],
            char_tiles[11],
        ]
    elif direction == 'right':
        dir_tiles = [
            char_tiles[6],
            char_tiles[7],
            char_tiles[6],
            char_tiles[8],
        ]
    elif direction == 'left':
        dir_tiles = [
            char_tiles[3],
            char_tiles[4],
            char_tiles[3],
            char_tiles[5],
        ]
    else:
        dir_tiles = [
            char_tiles[0]
            ]
    frames = list(zip(dir_tiles,
                      [150, 150, 150, 150]))
    animChar = pyganim.PygAnimation(frames)
    animChar.play()
    return animChar

@lru_cache(None)
def get_laundry_basin():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'food1.png'),
        rects=[(160, 285, 32, 35)])[0].convert_alpha()

@lru_cache(None)
def get_lemonade_glass():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'food1.png'),
        rects=[(196, 258, 10, 14)])[0].convert_alpha()

@lru_cache(None)
def get_lemonade_pitcher():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'food1.png'),
        rects=[(227, 290, 18, 21)])[0].convert_alpha()

@lru_cache(None)
def get_rat_poison():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'apothecary1.png'),
        rects=[(325, 224, 15, 17)])[0].convert_alpha()

@lru_cache(None)
def get_empty_bottle():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'apothecary1.png'),
        rects=[(272, 385, 15, 17)])[0].convert_alpha()


@lru_cache(None)
def get_lemonade_stand():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'food1.png'),
        rects=[(192, 161, 65, 86)])[0].convert_alpha()

@lru_cache(None)
def get_sock():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'fairytale1.png'),
        rects=[(259, 128, 20, 22)])[0].convert_alpha()

@lru_cache(None)
def get_stained_glass_window():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'fairytale2.png'),
        rects=[(225, 111, 31, 69)])[0].convert_alpha()

@lru_cache(None)
def get_desk():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'library1.png'),
        rects=[(192, 277, 64, 64)])[0].convert_alpha()

@lru_cache(None)
def get_prayer_edits():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'library1.png'),
        rects=[(415, 224, 34, 29)])[0].convert_alpha()

@lru_cache(None)
def get_prayer_scroll():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'library1.png'),
        rects=[(479, 223, 33, 34)])[0].convert_alpha()

@lru_cache(None)
def get_bridge():
    tiles = [
        (416, 32, 44, 32)
    ]
    images = pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'foliage1.png'),
        rects=tiles)
    for image in images:
        image.convert_alpha()
    bridge = pygame.Surface((124, 32), pygame.SRCALPHA, 32).convert_alpha()

    # bridge wide enough over river
    for i in range(0, 132, 44):
        bridge.blit(images[0], (i, 0))
    return bridge

@lru_cache(None)
def get_basin_water():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'food1.png'),
        rects=[(159, 157, 33, 38)])[0].convert_alpha()

@lru_cache(None)
def get_basin_empty():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'food2.png'),
        rects=[(159, 157, 33, 38)])[0].convert_alpha()

@lru_cache(None)
def get_dirt_path():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'foliage4.png'),
        rects=[(130, 0, 28, 32)])[0].convert_alpha()


@lru_cache(None)
def get_weed():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, "foliage2.png"),
        rects=[(131, 453, 58, 58)])[0].convert_alpha()


@lru_cache(None)
def get_walls(width):
    wall_tile = pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'walls2.png'),
        rects=[(64, 0, 64, 64)])[0].convert()
    wall = pygame.Surface((width, 64), pygame.SRCALPHA, 32).convert()
    for i in range(0, width, 64):
        wall.blit(wall_tile, (i, 0))
    return wall

@lru_cache(None)
def get_walls_edge(height):
    wall_tile = pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'walls2.png'),
        rects=[(64, 0, 12, 64)])[0].convert()
    wall = pygame.Surface((12, height), pygame.SRCALPHA, 32).convert()
    for i in range(0, height, 64):
        wall.blit(wall_tile, (0, i))
    return wall


@lru_cache(None)
def get_forest(width, height):
    tiles = [
        (0, 220, 130, 130),
        # this is the annoyingly long one in case you were wondering
        (258, 290, 125, 220),
        (130, 95, 120, 126),
        (133, 226, 120, 126)
    ]
    forest_tile = pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'foliage2.png'),
        rects=tiles)
    for tile in forest_tile:
        tile.convert_alpha()
    forest = pygame.Surface(
        (width, height), pygame.SRCALPHA, 32).convert_alpha()

    # for top edge
    for i in range(0, width, 100):
        forest.blit(forest_tile[1], (i, -50))
        forest.blit(random.choice(forest_tile),
                    (i+random.randint(-30, 0), 0+random.randint(-20, 20)))
        forest.blit(random.choice(forest_tile),
                    (i+random.randint(-30, 0), 150+random.randint(-20, 20)))
        forest.blit(random.choice([forest_tile[0], forest_tile[2], forest_tile[3]]), (
            i+random.randint(-25, 25), 250+random.randint(-25, 25)))
    # left edge
    for i in range(0, height, 100):
        forest.blit(forest_tile[1], (-50, i+random.randint(-30, 0)))
        for i_x in range(50, 450, 90):
            forest.blit(random.choice(forest_tile),
                        (i_x+random.randint(-30, 30), i+random.randint(-30, 0)))
    # right edge
    for i in range(0, height, 100):
        forest.blit(forest_tile[1], (width-100, i+random.randint(-30, 0)))
        for i_x in range(50, 550, 90):
            forest.blit(random.choice(forest_tile), ((width - i_x) +
                                                     random.randint(-30, 30), i+random.randint(-30, 0)))
    # bottom edge
    for i in range(0, width, 100):
        for i_y in range(50, 400, 90):
            forest.blit(random.choice(
                forest_tile), (i+random.randint(-30, 0), (width - i_y)+random.randint(-30, 30)))
        forest.blit(forest_tile[1], (i, height-100))
    return forest


@lru_cache(None)
def get_lemon():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, "food1.png"),
        rects=[(55, 180, 8, 8)])[0].convert_alpha()


@lru_cache(None)
def get_vegetables(width, height):
    tiles = [
        (10, 99, 41, 30),
        (10, 130, 41, 31),
        (10, 163, 41, 30),
        (10, 193, 41, 30),
        (10, 223, 41, 35),
        (10, 256, 41, 30)
    ]
    veg_tiles = pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, "food1.png"),
        rects=tiles)
    for tile in veg_tiles:
        tile.convert_alpha()
    vegetables = pygame.Surface(
        (width, height), pygame.SRCALPHA, 32).convert_alpha()
    for i in range(50, width-30, 30):
        vegetables.blit(random.choice(veg_tiles), (0, i))
        vegetables.blit(random.choice(veg_tiles), (width-40, i))
    return vegetables

@lru_cache(None)
def get_lemon_basket():
    tiles = [
        (10, 99, 41, 30),
        (10, 130, 41, 31),
        (10, 163, 41, 30),
        (10, 193, 41, 30),
        (10, 223, 41, 35),
        (10, 256, 41, 30)
    ]
    veg_tiles = pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, "food1.png"),
        rects=tiles)
    for tile in veg_tiles:
        tile.convert_alpha()
    vegetables = pygame.Surface(
        (42, 40), pygame.SRCALPHA, 32).convert_alpha()
    vegetables.blit(veg_tiles[2],(0,0))
    return vegetables

@lru_cache(None)
def get_stone_cross_floor(width, height):
    tiles = [
        (200, 340, 32, 32)
    ]
    height_prop = int((height - 32) * 7 / 16)
    images = pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'floors1.png'),
        rects=tiles)
    for image in images:
        image.convert_alpha()
    stone_floor = pygame.Surface((width, height), pygame.SRCALPHA, 32).convert_alpha()

    # long column
    for y in range(64, height, 32):
        for x in range(64, (width - 64), 32):
            stone_floor.blit(images[0], (x, y))

    # wide column
    for y in range(128, height_prop + 32, 32):
        for x in range(0, width, 32):
            stone_floor.blit(images[0], (x, y))
    return stone_floor

@lru_cache(None)
def get_stone_cross_wall(width, height):
    tiles = [
        (191, 84, 8, 16),
        (248, 84, 8, 16),
        (191, 84, 16, 8),
        (232, 84, 16, 8),
        (192, 204, 64, 32),
        (208, 204, 32, 32)
    ]

    height_prop = int((height - 32) * 7 / 16)
    images = pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'walls2.png'),
        rects=tiles)
    for image in images:
        image.convert_alpha()
    stone_wall = pygame.Surface((width, height), pygame.SRCALPHA, 32).convert_alpha()

    # top long column
    for y in range(64, 128, 16):
        stone_wall.blit(images[0], (64, y))
        stone_wall.blit(images[1], ((width - 72), y))

    # bottom long column
    for y in range(height_prop + 32, height, 16):
        stone_wall.blit(images[0], (64, y))
        stone_wall.blit(images[1], ((width - 72), y))

    # wide column sides
    for y in range(128, height_prop + 32, 16):
        stone_wall.blit(images[0], (0, y))
        stone_wall.blit(images[1], (width - 8, y))

    # wide column left
    for x in range(0, 64, 16):
        stone_wall.blit(images[2], (x, height_prop + 24))

    # wide column right
    for x in range(width - 64, width, 16):
        stone_wall.blit(images[2], (x, height_prop + 24))

    # top back wall
    for y in range(0, 64, 32):
        stone_wall.blit(images[4], (64, y))
        stone_wall.blit(images[5], (128, y))
        stone_wall.blit(images[4], (160, y))

    # wide column back wall left
    for x in range(0, 64, 64):
        stone_wall.blit(images[4], (x, 64))
        stone_wall.blit(images[4], (x, 96))


    for x in range(width - 64, width, 64):
        stone_wall.blit(images[4], (x, 64))
        stone_wall.blit(images[4], (x, 96))

    # bottom wall after entrance
    stone_wall.blit(images[2], (64, height - 8))
    stone_wall.blit(images[2], (80, height - 8))
    stone_wall.blit(images[2], (width - 80, height - 8))
    stone_wall.blit(images[2], ((width - 96), height - 8))
    stone_wall.blit(images[2], (96, height - 8))
    stone_wall.blit(images[2], (112, height - 8))
    stone_wall.blit(images[2], (width - 112, height - 8))
    stone_wall.blit(images[2], ((width - 128), height - 8))

    return stone_wall


@lru_cache(None)
def get_altar():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, "library1.png"),
        rects=[(352, 294, 36, 48)])[0].convert_alpha()


@lru_cache(None)
def get_pews():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, "foliage1.png"),
        rects=[(128, 460, 64, 16)])[0].convert_alpha()

@lru_cache(None)
def get_image_from_spirtes_dir(filename):
    return get_image(os.path.join(settings.SPRITES_DIR, filename), True)


@lru_cache(None)
def get_roof_small() -> pygame.Surface:
    return get_image_from_spirtes_dir("building_top1.png")

@lru_cache(None)
def get_church_roof() -> pygame.Surface:
    return get_image_from_spirtes_dir("Church_rooftop.png")

@lru_cache(None)
def get_conversation_box():
    return get_image_from_spirtes_dir("conversation_box.png")

@lru_cache(None)
def get_inventory_box():
    return get_image_from_spirtes_dir("inventory_box.png")

@lru_cache(None)
def get_info_box():
    return get_image_from_spirtes_dir("task_box.png")

@lru_cache(None)
def get_dirt(width: int, height: int) -> pygame.Surface:
    tiles = [
        (140, 45, 44, 44),
        (128, 35, 36, 33),
        (158, 35, 36, 33),
        (129, 63, 36, 35),
        (157, 63, 36, 35),
        (127, 46, 35, 35),
        (147, 35, 33, 33),
        (160, 51, 33, 33),
        (145, 65, 33, 33)
    ]
    dirt_tile = pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'foliage4.png'),
        rects=tiles)
    for tile in dirt_tile:
        tile.convert_alpha()
    dirt = pygame.Surface((width, height), pygame.SRCALPHA, 32).convert_alpha()

    for i in range(0, width, 33):
        for j in range(0, height, 33):
            dirt.blit(dirt_tile[5], (0, i))
            dirt.blit(dirt_tile[0], (i, j))
            dirt.blit(dirt_tile[7], (width-33, j))
        dirt.blit(dirt_tile[6], (i, 0))
        dirt.blit(dirt_tile[8], (i, height-30))
    dirt.blit(dirt_tile[1], (0,0))
    dirt.blit(dirt_tile[2], (width-33, 0))
    dirt.blit(dirt_tile[3], (0, height-33))
    dirt.blit(dirt_tile[4], (width-33, height-33))
    return dirt

@lru_cache(None)
def get_bed() -> pygame.Surface:
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, "apothecary1.png"),
        rects=[(192, 430, 32, 64)])[0].convert_alpha()

@lru_cache(None)
def get_sideways_bed() -> pygame.Surface:
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, "apothecary1.png"),
        rects=[(256, 186, 58, 38)])[0].convert_alpha()

@lru_cache(None)
def get_grave() -> pygame.Surface:
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, "foliage5.png"),
        rects=[(65, 131, 63, 60)])[0].convert_alpha()

@lru_cache(None)
def get_dug_grave() -> pygame.Surface:
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, "foliage6.png"),
        rects=[(65, 131, 63, 60)])[0].convert_alpha()

@lru_cache(None)
def get_planted_grave() -> pygame.Surface:
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, "grave.png"),
        rects=[(96, 144, 47, 46)])[0].convert_alpha()

@lru_cache(None)
def get_shovel() -> pygame.Surface:
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, "shovel.png"),
        rects=[(2, 2, 13, 50)])[0].convert_alpha()

@lru_cache(None)
def get_fire():
    tiles = [
        (0, 20, 64, 64),
        (64, 20, 64, 64),
        (128, 20, 64, 64)
    ]
    fire_tiles = pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, "fire3.png"),
        rects=tiles)
    frames = list(zip(fire_tiles,
                      [100, 100, 100]))
    animFire = pyganim.PygAnimation(frames)
    animFire.play()
    return animFire

@lru_cache(None)
def get_tool_sign():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'building_signs.png'),
        rects=[(240, 62, 48, 34)])[0].convert_alpha()

@lru_cache(None)
def get_clothes_sign():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'building_signs.png'),
        rects=[(96, 110, 48, 31)])[0].convert_alpha()

@lru_cache(None)
def get_stores_sign():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'building_signs.png'),
        rects=[(144, 110, 48, 31)])[0].convert_alpha()



@lru_cache(None)
def get_cage():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'attic1.png'),
        rects=[(482, 253, 31, 39)])[0].convert_alpha()

@lru_cache(None)
def get_carpet():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'attic1.png'),
        rects=[(100, 353, 90, 63)])[0].convert_alpha()

@lru_cache(None)
def get_cans():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'attic1.png'),
        rects=[(194, 222, 31, 39)])[0].convert_alpha()

@lru_cache(None)
def get_boxes():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'attic1.png'),
        rects=[(382, 35, 62, 64)])[0].convert_alpha()


@lru_cache(None)
def get_bear():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'attic1.png'),
        rects=[(291, 97, 27, 35)])[0].convert_alpha()


@lru_cache(None)
def get_library_sign():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'building_signs.png'),
        rects=[(144, 159, 48, 34)])[0].convert_alpha()

@lru_cache(None)
def get_painting():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'library1.png'),
        rects=[(34, 4, 63, 29)])[0].convert_alpha()

@lru_cache(None)
def get_shelf_m():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'library1.png'),
        rects=[(31, 42, 64,72)])[0].convert_alpha()

@lru_cache(None)
def get_shelf_l():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'library1.png'),
        rects=[(128, 46, 129,68)])[0].convert_alpha()

@lru_cache(None)
def get_laundry_dirty():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'attic1.png'),
        rects=[(10, 200, 53, 35)])[0].convert_alpha()

@lru_cache(None)
def get_laundry_clean_white():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'attic1.png'),
        rects=[(65, 201, 25, 24)])[0].convert_alpha()

@lru_cache(None)
def get_laundry_clean_pink():
    # pyganim.getImagesFromSpriteSheet(
    #     os.path.join(settings.SPRITES_DIR, 'attic1.png'),
    #     rects=[(6, 271, 24, 24)])[0].convert_alpha()
    image = get_laundry_clean_white()
    image.fill((16, 91, 38) + (0,), None, pygame.BLEND_RGB_SUB)
    return image


@lru_cache(None)
def get_laundry_clean_other():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'attic1.png'),
        rects=[(65, 261, 32, 232)])[0].convert_alpha()

@lru_cache(None)
def get_sugar():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'apothecary1.png'),
        rects=[(357, 391, 23, 16)])[0].convert_alpha()

@lru_cache(None)
def get_soap():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'apothecary1.png'),
        rects=[(235, 298, 19, 23)])[0].convert_alpha()

@lru_cache(None)
def get_gravestone1():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'grave.png'),
        rects=[(58, 341, 36, 48)])[0].convert_alpha()

@lru_cache(None)
def get_gravestone2():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'grave.png'),
        rects=[(57, 387, 38, 48)])[0].convert_alpha()

@lru_cache(None)
def get_gravestone3():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'grave.png'),
        rects=[(105, 338, 35, 48)])[0].convert_alpha()

@lru_cache(None)
def get_gravestone4():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'grave.png'),
        rects=[(105, 338, 35, 48)])[0].convert_alpha()

@lru_cache(None)
def get_gravestone5():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'grave.png'),
        rects=[(55, 49, 37, 51)])[0].convert_alpha()

@lru_cache(None)
def get_candles_black():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'attic1.png'),
        rects=[(70, 488, 21, 23)])[0].convert_alpha()

@lru_cache(None)
def get_candles_white():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'attic1.png'),
        rects=[(2, 487, 23, 26)])[0].convert_alpha()

@lru_cache(None)
def get_candles_pink():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'attic1.png'),
        rects=[(0, 456, 23, 26)])[0].convert_alpha()

@lru_cache(None)
def get_garden(width, height):
    tiles = [
        (3, 227, 31, 28),
        (32, 255, 31, 28),
        (65, 255, 35, 33),
        (66, 259, 62, 64),
        (8, 269, 53, 52),
        (132, 288, 59, 35),
    ]
    garden_tile = pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'foliage1.png'),
        rects=tiles)
    for tile in garden_tile:
        tile.convert_alpha()
    garden = pygame.Surface(
        (width, height), pygame.SRCALPHA, 32).convert_alpha()

    # for top edge
    for i in range(0, width, 60):
        garden.blit(random.choice(garden_tile),
                (i+random.randint(0, 5), 0+random.randint(0, 10)))
        garden.blit(random.choice(garden_tile),
                (i+random.randint(0, 5), 0+random.randint(0, 10)))
    for j in range(0, height, 60):
        garden.blit(random.choice(garden_tile),
                (0+random.randint(0, 10), j+random.randint(0, 5)))
        garden.blit(random.choice(garden_tile),
                (width-60+random.randint(0, 10), j+random.randint(0, 5)))
    return garden

@lru_cache(None)
def get_plant1():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'nature.png'),
        rects=[(241, 531, 47, 43)])[0].convert_alpha()

@lru_cache(None)
def get_plant2():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'nature.png'),
        rects=[(584, 143, 40, 45)])[0].convert_alpha()

@lru_cache(None)
def get_plant3():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'nature.png'),
        rects=[(342, 193, 35, 50)])[0].convert_alpha()

@lru_cache(None)
def get_plant4():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'nature.png'),
        rects=[(485, 478, 40, 54)])[0].convert_alpha()

@lru_cache(None)
def get_plant5():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'nature.png'),
        rects=[(344, 592, 28, 34)])[0].convert_alpha()

@lru_cache(None)
def get_plant6():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'nature.png'),
        rects=[(344, 592, 28, 34)])[0].convert_alpha()


@lru_cache(None)
def get_plant7():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'nature.png'),
        rects=[(59, 251, 33, 46)])[0].convert_alpha()

@lru_cache(None)
def get_herbs():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'apothecary1.png'),
        rects=[(256, 18, 58, 33)])[0].convert_alpha()

@lru_cache(None)
def get_cabinet():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'apothecary1.png'),
        rects=[(133, 10, 56, 71)])[0].convert_alpha()


@lru_cache(None)
def get_kitchen_sign():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'building_signs.png'),
        rects=[(0, 158, 48, 36)])[0].convert_alpha()

@lru_cache(None)
def get_bed_sign():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'building_signs2.png'),
        rects=[(144, 158, 48, 31)])[0].convert_alpha()


@lru_cache(None)
def get_sheet():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'apothecary1.png'),
        rects=[(278, 227, 40, 30)])[0].convert_alpha()

@lru_cache(None)
def get_clothes_line():
    return get_image_from_spirtes_dir('clothes_line.png')

@lru_cache(None)
def get_demon():
    tiles = [
        (290, 129, 30, 34),
        (322, 129, 30, 34),
        (355, 129, 30, 34)
    ]
    demon_tiles = pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, "chars6.png"),
        rects=tiles)
    frames = list(zip(demon_tiles,
                      [100, 100, 100]))
    animdemon = pyganim.PygAnimation(frames)
    animdemon.play()
    return animdemon

@lru_cache(None)
def get_demon_fire():
    tiles = [
        (0, 0, 100, 100),
        (0, 100, 100, 100),
        (0, 200, 100, 100),
        (0, 300, 100, 100),
        (0, 400, 100, 100),
        (0, 500, 100, 100),
        (0, 600, 100, 100),
        (0, 700, 100, 100),
        (100, 0, 100, 100),
        (100, 100, 100, 100),
        (100, 200, 100, 100),
        (100, 300, 100, 100),
        (100, 400, 100, 100),
        (100, 500, 100, 100),
        (100, 600, 100, 100),
        (100, 700, 100, 100),
        (200, 0, 100, 100),
        (200, 100, 100, 100),
        (200, 200, 100, 100),
        (200, 300, 100, 100),
        (200, 400, 100, 100),
    ]
    demon_tiles = pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, "sunburst.png"),
        rects=tiles)
    frames = list(zip(demon_tiles,
                      [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]))
    animdemon = pyganim.PygAnimation(frames)
    animdemon.play()
    return animdemon

@lru_cache(None)
def get_melted_wax():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'apothecary1.png'),
        rects=[(419, 68, 27, 26)])[0].convert_alpha()

@lru_cache(None)
def get_brown_jar():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'apothecary1.png'),
        rects=[(393, 327, 15, 17)])[0].convert_alpha()

@lru_cache(None)
def get_pestle_and_mortar():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'apothecary1.png'),
        rects=[(422, 224, 21, 20)])[0].convert_alpha()

@lru_cache(None)
def get_pentagram():
    return pyganim.getImagesFromSpriteSheet(
        os.path.join(settings.SPRITES_DIR, 'pentagram.png'),
        rects=[(0, 0, 800, 800)])[0].convert_alpha()
