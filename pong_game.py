import pygame
import sys

# Inizializza Pygame
pygame.init()

# Definisci costanti per le dimensioni della finestra e i colori
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
WHITE = (255, 255, 255)

# Crea la finestra di gioco
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pong")

# Inizializza le variabili per le racchette e la palla
paddle_width = 10
paddle_height = 100
paddle_speed = 5
player1_x = 50
player1_y = (WINDOW_HEIGHT - paddle_height) // 2
player2_x = WINDOW_WIDTH - 50 - paddle_width
player2_y = (WINDOW_HEIGHT - paddle_height) // 2

ball_x = WINDOW_WIDTH // 2
ball_y = WINDOW_HEIGHT // 2
ball_speed_x = 5
ball_speed_y = 5

# Loop principale del gioco
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimento delle racchette
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_y > 0:
        player1_y -= paddle_speed
    if keys[pygame.K_s] and player1_y < WINDOW_HEIGHT - paddle_height:
        player1_y += paddle_speed

    if keys[pygame.K_UP] and player2_y > 0:
        player2_y -= paddle_speed
    if keys[pygame.K_DOWN] and player2_y < WINDOW_HEIGHT - paddle_height:
        player2_y += paddle_speed

    # Movimento della palla
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Controllo delle collisioni con le pareti superiori e inferiori
    if ball_y <= 0 or ball_y >= WINDOW_HEIGHT:
        ball_speed_y = -ball_speed_y

    # Controllo delle collisioni con le racchette
    if (
        player1_x + paddle_width >= ball_x >= player1_x
        and player1_y + paddle_height >= ball_y >= player1_y
    ) or (
        player2_x <= ball_x <= player2_x + paddle_width
        and player2_y + paddle_height >= ball_y >= player2_y
    ):
        ball_speed_x = -ball_speed_x

    # Controllo dei punti segnati
    if ball_x <= 0 or ball_x >= WINDOW_WIDTH:
        ball_x = WINDOW_WIDTH // 2
        ball_y = WINDOW_HEIGHT // 2
        ball_speed_x = -ball_speed_x

    # Pulisce la schermata e disegna gli oggetti
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, WHITE, (player1_x, player1_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, WHITE, (player2_x, player2_y, paddle_width, paddle_height))
    pygame.draw.ellipse(screen, WHITE, (ball_x, ball_y, 10, 10))

    # Aggiorna la schermata
    pygame.display.update()
