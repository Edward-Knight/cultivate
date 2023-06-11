import contextlib
# don't print pygame welcome
with contextlib.redirect_stdout(None):
    import pygame
import pyganim


def getImagesFromSpriteSheet(filename, width=None, height=None, rows=None, cols=None, rects=None):
    """Loads several sprites from a single image file (a "spritesheet").

    One (and only one) of the following parameters should be specified:
        * width & height of each sprite (all must be the same size)
        * number of rows and columns of sprites (all must be the same size)
        * rects, which is a list of tuples formatted as (pygame.Rect, index) or (left, top, width, height)

    This is a patched version of the getImagesFromSpriteSheet from pyganim 1.9.2 (git hash 4ae3004),
    that changes only this line:
        surf = pygame.Surface((rect[2], rect[3]), 0, sheetImage) # create Surface with width/height in rect
    to:
        surf = pygame.Surface((rect[2], rect[3]), pygame.SRCALPHA, sheetImage) # create Surface with width/height in rect
    This fixes blitting sprites with alpha values for me on AArch64 macOS using pygame 2 / SDL2.
    """

    argsType = '' # there should be exactly 1 set of arguments passed (i.e. don't pass width/height AND rows/cols)
    if (width is not None or height is not None) and (argsType == ''):
        argsType = 'width/height'
        assert width is not None and height is not None, 'Both width and height must be specified'
        assert type(width) == int and width > 0, 'width arg must be a non-zero positive integer'
        assert type(height) == int and height > 0, 'height arg must be a non-zero positive integer'
    if (rows is not None or cols is not None) and (argsType == ''):
        argsType = 'rows/cols'
        assert rows is not None and cols is not None, 'Both rows and cols must be specified'
        assert type(rows) == int and rows > 0, 'rows arg must be a non-zero positive integer'
        assert type(cols) == int and cols > 0, 'cols arg must be a non-zero positive integer'
    if (rects is not None) and (argsType == ''):
        argsType = 'rects'
        for i, rect in enumerate(rects):
            assert len(rect) == 4, 'rect at index %s is not a sequence of four ints: (left, top, width, height)' % (i)

            assert (type(rect[0]), type(rect[1]), type(rect[2]), type(rect[3])) == (int, int, int, int), 'rect '
    if argsType == '':
        raise ValueError('Only pass one set of args: width & height, rows & cols, *or* rects')

    sheetImage = pygame.image.load(filename).convert_alpha()

    if argsType == 'width/height':
        for y in range(0, sheetImage.get_height(), (sheetImage.get_height() // height)):
            if y + height > sheetImage.get_height():
                continue
            for x in range(0, sheetImage.get_width(), (sheetImage.get_width() // width)):
                if x + width > sheetImage.get_width():
                    continue

                rects.append((x, y, width, height))

    if argsType == 'rows/cols':
        spriteWidth = sheetImage.get_width() // cols
        spriteHeight = sheetImage.get_height() // rows

        for y in range(0, sheetImage.get_height(), spriteHeight):
            if y + spriteHeight > sheetImage.get_height():
                continue
            for x in range(0, sheetImage.get_width(), spriteWidth):
                if x + spriteWidth > sheetImage.get_width():
                    continue

                rects.append((x, y, spriteWidth, spriteHeight))

    # create a list of Surface objects from the sprite sheet
    returnedSurfaces = []
    for rect in rects:
        surf = pygame.Surface((rect[2], rect[3]), pygame.SRCALPHA, sheetImage) # create Surface with width/height in rect
        surf.blit(sheetImage, (0, 0), rect, pygame.BLEND_RGBA_ADD)
        returnedSurfaces.append(surf)

    return returnedSurfaces


pyganim.getImagesFromSpriteSheet = getImagesFromSpriteSheet
