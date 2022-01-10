import pygame
import random
pygame.font.init()

width, height = 900, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")

player_width, player_height = 10, 70
velocity = 5
ball_velocity_x = 5 * random.choice((1, -1))
ball_velocity_y = 5 * random.choice((1, -1))
left_score = 0
right_score = 0

left_player = pygame.Rect(10, height//2 -35, player_width, player_height)
right_player = pygame.Rect(880, height//2 -35, player_width, player_height)
ball = pygame.Rect(width//2 - 8, height//2 - 8, 16, 16)
border = pygame.Rect(width//2 - 1, 0, 2, height)
score_font = pygame.font.SysFont('comicsans', 25)
winner_font = pygame.font.SysFont('comicsans', 75)

def draw_window(left_score, right_score):
    window.fill((51, 51, 51))
    pygame.draw.rect(window, (13, 13, 13), border)
    pygame.draw.rect(window, (255, 140, 0), left_player)
    pygame.draw.rect(window, (255, 140, 0), right_player)
    pygame.draw.ellipse(window, (255, 140, 0), ball)
    left_score_text = score_font.render(str(left_score), 1, (13, 13, 13))
    right_score_text = score_font.render(str(right_score), 1, (13, 13, 13))
    window.blit(left_score_text, (255, 25))
    window.blit(right_score_text, (675, 25))
    pygame.display.update()

def left_movement(keys_pressed):
    if keys_pressed[pygame.K_w] and left_player.y - velocity > 5:
        left_player.y -= velocity
    if keys_pressed[pygame.K_s] and left_player.y + velocity + player_height < height - 5:
        left_player.y += velocity

def right_movement(keys_pressed):
    if keys_pressed[pygame.K_UP] and right_player.y - velocity > 5:
        right_player.y -= velocity
    if keys_pressed[pygame.K_DOWN] and right_player.y + velocity + player_height < height - 5:
        right_player.y += velocity

def ball_movement():
    global ball_velocity_x, ball_velocity_y, left_score, right_score
    ball.x += ball_velocity_x
    ball.y += ball_velocity_y
    if ball.top <= 0 or ball.bottom >= height:
        ball_velocity_y *= -1
    if ball.left <= 0:
        right_score += 1
        game_restart()
    if ball.right >= width:
        left_score += 1
        game_restart()
    if ball.colliderect(left_player) or ball.colliderect(right_player):
        ball_velocity_x *= -1
    
def game_restart():
    global ball_velocity_x, ball_velocity_y, left_player, right_player
    ball.center = (width//2, height//2)
    ball_velocity_x *= random.choice((1, -1))
    ball_velocity_y *= random.choice((1, -1))
    left_player = pygame.Rect(10, height//2 -35, player_width, player_height)
    right_player = pygame.Rect(880, height//2 -35, player_width, player_height)
    pygame.time.delay(500)

def draw_winner(winner_text):
    draw_text = winner_font.render(winner_text, 1, (0, 0, 0))
    window.blit(draw_text, (width//2 - draw_text.get_width()//2, height//2 - draw_text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(5000)

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick((60))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        winner_text = ""
        if left_score >= 10:
            winner_text = "Left Player Wins!"
        if right_score >= 10:
            winner_text = "Right Player Wins!"
        if winner_text != "":
            draw_winner(winner_text)
            break
        keys_pressed = pygame.key.get_pressed()
        left_movement(keys_pressed)
        right_movement(keys_pressed)
        ball_movement()
        draw_window(left_score, right_score)
    pygame.quit()

if __name__ == "__main__":
    main()