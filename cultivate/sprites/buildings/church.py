import pygame
from cultivate.loader import get_stone_cross_floor, get_stone_cross_wall, get_altar


class Church:
    def __init__(self, map_background: pygame.Surface):
        self.rect = pygame.Rect(1000, 1000, 288, 544)
        self.floor = get_stone_cross_floor(self.rect.w, self.rect.h)
        self.walls = get_stone_cross_wall(288, 544)
        #self.lemon = get_lemon()
        self.altar = get_altar()
        map_background.blit(self.floor, (self.rect.x, self.rect.y))
        map_background.blit(self.walls, (self.rect.x, self.rect.y))
        # map_background.blit(self.lemon, (self.rect.x, self.rect.y))
        map_background.blit(self.altar, (1128, (int((544 - 32) * 7 / 16) + 904)))
        # self.roof = get_roof_small()

    def draw(self, map_foreground: pygame.Surface, viewport: pygame.Rect):
        #rect_near_player = pygame.Rect(viewport.centerx, viewport.centery, 200, 200)
        # draw if the building is on screen but not near the player
       #if viewport.colliderect(self.rect) and not self.rect.colliderect(rect_near_player):
       #    map_foreground.blit(
       #        self.roof,
       #        pygame.Rect(self.rect.x - viewport.x, self.rect.y - viewport.y,
       #                    self.rect.width, self.rect.height)
       #    )
        pass