# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 11:16:23 2025

Enlever la variable   dans les class

timer   

@author: cdelor
"""

import pygame, math, sys, random
#from pathlib import Path

WIDTH, HEIGHT = 800, 600
FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (80, 220, 100)
RED = (220, 80, 80)
VERT = (0, 150, 0)
ROSE_PALE = [(255, 200, 193), (255, 180, 193), (255, 160, 193), (255, 140, 193)]
BORDEAUX = [(180, 50, 70),(150, 30, 60),(120, 20, 50),(90, 10, 40)]
JAUNE = (250, 200, 0)
PLAYING, GAME_OVER = 0, 1



compteur = 0

a= 150
LARGEUR = 400
HAUTEUR = 300
COULEUR_FOND = (0, 0, 0)
couleur_cercle2 = (0, 255, 0)
clock = pygame.time.Clock()
taille1 = random.randint(0,10)
pos_x = -20
pos_x2 = -20
d_x = 4
d_x2 = 2
taille2= 1000

#ASSETS = Path(__file__).parent / "assets"



# --- FONCTION FLEUR --- #
def fleurjoueur(surface, x, y):
    


    num_petales = 6
    largeur_petale, hauteur_petale = 16, 30

    for n, couleur in enumerate(ROSE_PALE):
        for i in range(num_petales):
            angle_deg = i * (360 / num_petales)
            angle_rad = math.radians(angle_deg)
            petale_x = x + math.cos(angle_rad) * 20
            petale_y = y + math.sin(angle_rad) * 20

            petale_surface = pygame.Surface((largeur_petale, hauteur_petale), pygame.SRCALPHA)
            pygame.draw.ellipse(petale_surface, couleur, (0, 0, largeur_petale, hauteur_petale))
            petale_surface = pygame.transform.rotate(petale_surface, 90 - angle_deg + n * 20)
            petale_rect = petale_surface.get_rect(center=(int(petale_x), int(petale_y)))
            surface.blit(petale_surface, petale_rect)

    # Centre jaune
    pygame.draw.circle(surface, JAUNE, (x, y), 7)
    
def fleurennemie(surface, x, y):

    num_petales = 6
    largeur_petale, hauteur_petale = 16, 30

    for n, couleur in enumerate(BORDEAUX):
        for i in range(num_petales):
            angle_deg = i * (360 / num_petales)
            angle_rad = math.radians(angle_deg)
            petale_x = x + math.cos(angle_rad) * 20
            petale_y = y + math.sin(angle_rad) * 20

            petale_surface = pygame.Surface((largeur_petale, hauteur_petale), pygame.SRCALPHA)
            pygame.draw.ellipse(petale_surface, couleur, (0, 0, largeur_petale, hauteur_petale))
            petale_surface = pygame.transform.rotate(petale_surface, 90 - angle_deg + n * 50)
            petale_rect = petale_surface.get_rect(center=(int(petale_x), int(petale_y)))
            surface.blit(petale_surface, petale_rect)

    # Centre jaune
    pygame.draw.circle(surface, JAUNE, (x, y), 7)

def fleurennemie2(surface, x, y):

    num_petales = 6
    largeur_petale, hauteur_petale = 16, 30

    for n, couleur in enumerate(BORDEAUX):
        for i in range(num_petales):
            angle_deg = i * (360 / num_petales)
            angle_rad = math.radians(angle_deg)
            petale_x = x + math.cos(angle_rad) * 20
            petale_y = y + math.sin(angle_rad) * 20

            petale_surface = pygame.Surface((largeur_petale, hauteur_petale), pygame.SRCALPHA)
            pygame.draw.ellipse(petale_surface, couleur, (0, 0, largeur_petale, hauteur_petale))
            petale_surface = pygame.transform.rotate(petale_surface, 90 - angle_deg + n * 40)
            petale_rect = petale_surface.get_rect(center=(int(petale_x), int(petale_y)))
            surface.blit(petale_surface, petale_rect)

    # Centre jaune
    pygame.draw.circle(surface, JAUNE, (x, y), 7)



# --- SPRITES --- #
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed=-8):
        super().__init__()
        self.image = pygame.Surface((4, 12))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(midbottom=(x, y))
        self.speed = speed

    def update(self, *_):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Surface transparente pour la fleur
        self.image = pygame.Surface((80, 80), pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 0))  # fond transparent
        fleurennemie(self.image, 35, 35)  # dessin centré dans la surface
        self.rect = self.image.get_rect(topleft=(x, y))
        
        
class Enemy2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Surface transparente pour la fleur
        self.image = pygame.Surface((80, 80), pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 0))  # fond transparent
        fleurennemie2(self.image, 35, 35)  # dessin centré dans la surface
        self.rect = self.image.get_rect(topleft=(x, y))



class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, speed=5):
        super().__init__()
        self.image = pygame.Surface((80, 80), pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 0))  # fond transparent
        fleurjoueur(self.image, 35, 35)  # dessin centré dans la surface
        self.rect = self.image.get_rect(midbottom=(x, y))
        self.speed = speed
        self.shoot_cooldown = 250
        self.last_shot = 0
        self.lives = 3

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        self.rect.left = max(self.rect.left, 0)
        self.rect.right = min(self.rect.right, WIDTH)

    def can_shoot(self):
        return pygame.time.get_ticks() - self.last_shot >= self.shoot_cooldown

    def shoot(self, bullets_group, all_sprites_group):
        if self.can_shoot():
            bullet = Bullet(self.rect.centerx, self.rect.top)
            bullets_group.add(bullet)
            all_sprites_group.add(bullet)
            self.last_shot = pygame.time.get_ticks()


# --- JEU --- #
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Space Invaders - Fleurs 🌸")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 32)
        self.reset()


    def reset(self):
        self.all_sprites = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        
        global taille1, pos_x, pos_x2
        taille1 = random.randint(0, 10)
        pos_x = -20
        pos_x2 = -20

        self.player = Player(WIDTH // 2, HEIGHT - 30)
        self.all_sprites.add(self.player)
        
        #self.background = self.load_image("Fond.jpg",(WIDTH,HEIGHT))
        #self.player_img = self.load_image("Player.jpg",(60,60), WIDTH, HEIGHT)
        #self.enemy_img = self.load_image("red.jpg")

        # Grille d'ennemis (fleurs)
        for row in range(3):
            for col in range(5):
                e = Enemy(60 + col * 70, 60 + row * 80)
                self.enemies.add(e)
                self.all_sprites.add(e)
                f = Enemy2(410 + col * 70, 60 + row * 80)
                self.enemies.add(f) 
                self.all_sprites.add(f)

        self.fleet_dir = 1 
        self.fleet_speed = 1.0
        self.drop_amount = 15
        self.state = PLAYING
        self.score = 0

    def run(self):
        while True:
            self.clock.tick(FPS)
            self.handle_events()
            self.update()
            self.draw( )

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if self.state == PLAYING and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.player.shoot(self.bullets, self.all_sprites)
            if self.state == GAME_OVER and event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                self.reset()     
    #def load_image(self, filename, size = None, colorkey= None):
       # path = ASSETS / filename
        #if not path.exists():
         #   print("Fichier introuvable: {path}")
          #  surf = pygame.Surface(size or (50,50))
           # surf.fill(RED)
            #return surf
        #img = pygame.image.load(path).convert()
        #if colorkey is not None:
         #   img.set_colorkey(colorkey)
        #if size:
         #   img = pygame.transform.smoothscale(img,size)
        #return img
                
                
    def draw(self):
        
        self.screen.fill((0, 0+0.5* self.score, 0 +0.5* self.score))
        global pos_x, pos_x2, taille1, taille2, a, compteur
        if compteur:
            taille1 =  taille1 + 0.025* (taille2 -taille1)
            a = a + 0.05* (0 - a)
        if compteur ==2:
            taille1 = 5
            a=150
            compteur = 0
        for i in range (2,10):
            xal = random.randint(-400,400)
            yal= random.randint(-300,300)
            
            pygame.draw.circle(self.screen, couleur_cercle2, (i*(50*math.cos(0.05*pos_x )+ HEIGHT// 2)-400, i*pos_x2), 5*abs(math.cos(0.05*pos_x )))
            pygame.draw.circle(self.screen, couleur_cercle2, (pos_x2, HEIGHT // 2), 40)
        pos_x = (pos_x + d_x) % WIDTH
        
        pos_x2 = (pos_x2 + d_x2) % WIDTH
        pygame.draw.circle(self.screen, (0,0,a), ( WIDTH//2, HEIGHT// 2),taille1 )
        self.all_sprites.draw(self.screen)
        
        
        
        score_surf = self.font.render(f"Score: {self.score}", True, WHITE)
        lives_surf = self.font.render(f"Vies: {self.player.lives}", True, WHITE)
        compteur_surf = self.font.render(f"Compteur: {compteur}", True, WHITE)
        self.screen.blit(score_surf, (10, 10))
        self.screen.blit(compteur_surf, (10, 50))
        self.screen.blit(lives_surf, (WIDTH - 120, 10))

        if self.state == GAME_OVER:
            msg = self.font.render("FIN — Appuie sur R pour recommencer", True, WHITE)
            rect = msg.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            self.screen.blit(msg, rect)
            
        pygame.display.flip()
            
    def update(self):
        global compteur
        
        
        keys = pygame.key.get_pressed()
        if self.state != PLAYING:
            return

        self.all_sprites.update(keys)
        edge_hit = False
        for e in self.enemies:
            e.rect.x += self.fleet_dir * self.fleet_speed
            if e.rect.right >= WIDTH - 5 or e.rect.left <= 5:
                edge_hit = True
        if edge_hit:
            self.fleet_dir *= -1
            for e in self.enemies:
                e.rect.y += self.drop_amount
                
        for e in self.enemies:
            e.rect.x += self.fleet_dir * self.fleet_speed

        self.hits = pygame.sprite.groupcollide(self.enemies, self.bullets, True, True)
        self.score += len(self.hits) * 10
        
        
        if self.hits:
            compteur+=1

        for e in self.enemies:
            if e.rect.bottom >= HEIGHT - 40:
                self.state = GAME_OVER
            if e.rect.colliderect(self.player.rect):
                self.player.lives -= 1
                self.state = GAME_OVER

        if not self.enemies:
            self.state = GAME_OVER





if __name__ == "__main__":
    Game().run()
