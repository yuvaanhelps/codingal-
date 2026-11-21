

import pygame
import random
import math
import sys

pygame.init()

# SCREEN
WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SPACE INVADERS 3D")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 28, bold=True)
big_font = pygame.font.SysFont("Arial", 65, bold=True)

# COLORS
BLACK = (3, 5, 20)
WHITE = (255, 255, 255)
CYAN = (0, 220, 255)
RED = (255, 50, 70)
GREEN = (50, 255, 120)
PURPLE = (160, 70, 255)
YELLOW = (255, 230, 50)

# GAME VARIABLES
score = 0
lives = 3
level = 1
game_over = False
started = False
paused = False

player_x = WIDTH // 2
player_y = HEIGHT - 90
player_speed = 7

bullets = []
enemy_bullets = []
enemies = []
particles = []

enemy_direction = 1
enemy_speed = 1.2

# STARS
stars = [
    [random.randrange(WIDTH), random.randrange(HEIGHT),
     random.uniform(1, 3)]
    for _ in range(130)
]

# PLANET
planet_angle = 0


def create_enemies():
    global enemies
    enemies = []

    for row in range(4):
        for col in range(9):
            enemies.append({
                "x": 100 + col * 95,
                "y": 100 + row * 65,
                "row": row,
                "alive": True
            })


def draw_text(text, font_type, color, x, y, center=True):
    image = font_type.render(text, True, color)
    rect = image.get_rect()

    if center:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)

    screen.blit(image, rect)


def draw_background():
    global planet_angle

    screen.fill(BLACK)

    # Stars
    for star in stars:
        pygame.draw.circle(
            screen, WHITE,
            (int(star[0]), int(star[1])),
            max(1, int(star[2] / 2))
        )

        star[1] += star[2]

        if star[1] > HEIGHT:
            star[0] = random.randrange(WIDTH)
            star[1] = 0

    # Distant planet
    planet_angle += 0.01

    pygame.draw.circle(screen, (35, 25, 100),
                       (820, 150), 75)

    pygame.draw.arc(
        screen, PURPLE,
        (735, 115, 170, 80),
        planet_angle, planet_angle + math.pi,
        4
    )

    pygame.draw.circle(screen, (90, 65, 170),
                       (800, 125), 12)


def draw_player(x, y):
    # Spaceship shadow
    pygame.draw.ellipse(
        screen, (10, 50, 90),
        (x - 42, y + 18, 84, 18)
    )

    # Ship body
    pygame.draw.polygon(
        screen, CYAN,
        [
            (x, y - 35),
            (x - 35, y + 25),
            (x, y + 12),
            (x + 35, y + 25)
        ]
    )

    # Cockpit
    pygame.draw.ellipse(
        screen, WHITE,
        (x - 9, y - 10, 18, 25)
    )

    # Wings
    pygame.draw.polygon(
        screen, (0, 100, 220),
        [(x - 35, y + 15),
         (x - 55, y + 35),
         (x - 15, y + 25)]
    )

    pygame.draw.polygon(
        screen, (0, 100, 220),
        [(x + 35, y + 15),
         (x + 55, y + 35),
         (x + 15, y + 25)]
    )

    # Engine
    pygame.draw.circle(screen, YELLOW, (x, y + 30), 7)


def draw_enemy(enemy):
    x = int(enemy["x"])
    y = int(enemy["y"])

    color = [RED, GREEN, PURPLE, YELLOW][enemy["row"]]

    # Body
    pygame.draw.ellipse(
        screen, color,
        (x - 23, y - 17, 46, 35)
    )

    # Eyes
    pygame.draw.circle(screen, WHITE, (x - 10, y - 4), 6)
    pygame.draw.circle(screen, WHITE, (x + 10, y - 4), 6)

    pygame.draw.circle(screen, BLACK, (x - 10, y - 4), 3)
    pygame.draw.circle(screen, BLACK, (x + 10, y - 4), 3)

    # Alien legs
    pygame.draw.line(screen, color,
                     (x - 15, y + 15), (x - 25, y + 27), 5)
    pygame.draw.line(screen, color,
                     (x + 15, y + 15), (x + 25, y + 27), 5)


def create_explosion(x, y):
    for _ in range(15):
        particles.append({
            "x": x,
            "y": y,
            "dx": random.uniform(-4, 4),
            "dy": random.uniform(-4, 4),
            "life": 25
        })


def update_explosions():
    for p in particles[:]:
        p["x"] += p["dx"]
        p["y"] += p["dy"]
        p["life"] -= 1

        if p["life"] <= 0:
            particles.remove(p)
        else:
            pygame.draw.circle(
                screen, YELLOW,
                (int(p["x"]), int(p["y"])),
                4
            )


def reset_game():
    global score, lives, level, game_over
    global bullets, enemy_bullets, player_x

    score = 0
    lives = 3
    level = 1
    game_over = False
    player_x = WIDTH // 2

    bullets = []
    enemy_bullets = []

    create_enemies()


create_enemies()

running = True

while running:

    clock.tick(60)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                paused = not paused

            if event.key == pygame.K_SPACE:

                if not started:
                    started = True

                elif game_over:
                    reset_game()

                elif not paused:
                    bullets.append([
                        player_x, player_y - 35
                    ])

            if event.key == pygame.K_r and game_over:
                reset_game()

    keys = pygame.key.get_pressed()

    draw_background()

    if not started:

        draw_text("SPACE INVADERS 3D",
                  big_font, CYAN, WIDTH // 2, 220)

        draw_text("PRESS SPACE TO START",
                  font, WHITE, WIDTH // 2, 350)

        draw_text("ARROWS TO MOVE | SPACE TO SHOOT",
                  font, YELLOW, WIDTH // 2, 410)

    elif paused:

        draw_text("PAUSED", big_font,
                  YELLOW, WIDTH // 2, HEIGHT // 2)

        draw_text("PRESS ESC TO RESUME",
                  font, WHITE, WIDTH // 2, HEIGHT // 2 + 70)

    elif not game_over:

        # PLAYER MOVEMENT
        if keys[pygame.K_LEFT]:
            player_x -= player_speed

        if keys[pygame.K_RIGHT]:
            player_x += player_speed

        player_x = max(40, min(WIDTH - 40, player_x))

        draw_player(player_x, player_y)

        # BULLETS
        for bullet in bullets[:]:

            bullet[1] -= 12

            pygame.draw.line(
                screen, CYAN,
                (bullet[0], bullet[1]),
                (bullet[0], bullet[1] + 20), 5
            )

            if bullet[1] < 0:
                bullets.remove(bullet)

        # ENEMIES
        alive_enemies = [e for e in enemies if e["alive"]]

        for enemy in alive_enemies:

            enemy["x"] += enemy_direction * enemy_speed

            if enemy["x"] > WIDTH - 35 or enemy["x"] < 35:
                enemy_direction *= -1
                for e in alive_enemies:
                    e["y"] += 18
                break

            draw_enemy(enemy)

        # BULLET COLLISIONS
        for bullet in bullets[:]:

            for enemy in enemies:

                if enemy["alive"]:

                    distance = math.hypot(
                        bullet[0] - enemy["x"],
                        bullet[1] - enemy["y"]
                    )

                    if distance < 30:

                        enemy["alive"] = False
                        score += 10

                        create_explosion(
                            enemy["x"], enemy["y"]
                        )

                        if bullet in bullets:
                            bullets.remove(bullet)

                        break

        # ENEMY SHOOTING
        if random.random() < 0.025 and alive_enemies:

            shooter = random.choice(alive_enemies)

            enemy_bullets.append([
                shooter["x"], shooter["y"] + 20
            ])

        for bullet in enemy_bullets[:]:

            bullet[1] += 6

            pygame.draw.circle(
                screen, RED,
                (int(bullet[0]), int(bullet[1])), 6
            )

            if bullet[1] > HEIGHT:
                enemy_bullets.remove(bullet)
                continue

            if math.hypot(
                bullet[0] - player_x,
                bullet[1] - player_y
            ) < 35:

                lives -= 1
                enemy_bullets.remove(bullet)

                if lives <= 0:
                    game_over = True

        # ENEMY REACHES PLAYER
        if any(e["y"] > player_y - 45 for e in alive_enemies):
            game_over = True

        # NEXT LEVEL
        if not alive_enemies:

            level += 1
            enemy_speed += 0.4
            bullets.clear()
            enemy_bullets.clear()
            create_enemies()

        update_explosions()

        # HUD
        draw_text(f"SCORE: {score}", font,
                  WHITE, 20, 20, False)

        draw_text(f"LIVES: {lives}", font,
                  GREEN, 20, 60, False)

        draw_text(f"LEVEL: {level}", font,
                  YELLOW, 20, 100, False)

    else:

        update_explosions()

        draw_text("GAME OVER", big_font,
                  RED, WIDTH // 2, 250)

        draw_text(f"FINAL SCORE: {score}",
                  font, WHITE, WIDTH // 2, 350)

        draw_text("PRESS SPACE OR R TO RESTART",
                  font, YELLOW, WIDTH // 2, 420)

    pygame.display.flip()

pygame.quit()
sys.exit()
