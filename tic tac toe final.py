import pygame
import sys

# Počítá všechny způsoby výher a také když už není místo na tom. 
# Logika
def check_win(mas, sign):
    zeroes = 0  
    for row in mas:
        zeroes += row.count(0)
        if row.count(sign) == 3:
            return sign
    for col in range(3):
        if mas[0][col] == sign and mas[1][col] == sign and mas[2][col] == sign:
            return sign
    
    if mas[0][0] == sign and mas[1][1] == sign and mas[2][2] == sign:
            return sign
    if mas[0][2] == sign and mas[1][1] == sign and mas[2][0] == sign:
            return sign
    if zeroes == 0:
        return 'Piece'
    return False
        
pygame.init()
size_block = 100 
margin = 15
width = height = size_block * 3 + margin * 4

size_winwod = (width, height)
screen = pygame.display.set_mode(size_winwod)
pygame.display.set_caption("Tic Tac Toe")

black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
mas = [[0] * 3 for i in range(3)]

query = 0

# ----------------- Přidáno pro úvodní obrazovku -----------------
# Zobrazíme pravidla před začátkem hry
screen.fill(black)  # Černé pozadí

# Nastavení písma pro pravidla
font_large = pygame.font.SysFont('stxingkai', 30)  # Velké písmo pro nadpis
font_small = pygame.font.SysFont('stxingkai', 20)  # Menší písmo pro pravidla
text1 = font_large.render("Welcome to Tic Tac Toe", True, white)
text2 = font_small.render("GAME RULES:", True, white)
text3 = font_small.render("Each player can place one mark (or stone)", True, white)
text4 = font_small.render("per turn on the 3x3 grid. The WINNER is", True, white)
text5 = font_small.render("who succeeds in placing three of their", True, white)
text6 = font_small.render("marks in a:", True, white)
text7 = font_small.render("* horizontal,", True, white)
text8 = font_small.render("* vertical or", True, white)
text9 = font_small.render("* diagonal row", True, white)
text10 = font_small.render("Let's start the game (press Enter)", True, white)

# Výpis textu na obrazovku
screen.blit(text1, (width // 2 - text1.get_width() // 2, height // 8))
screen.blit(text2, (width // 2 - text2.get_width() // 2, height // 8 + 40))  # Zmenšený rozestup
screen.blit(text3, (width // 2 - text3.get_width() // 2, height // 8 + 70))  # Zmenšený rozestup
screen.blit(text4, (width // 2 - text4.get_width() // 2, height // 8 + 100))  # Zmenšený rozestup
screen.blit(text5, (width // 2 - text5.get_width() // 2, height // 8 + 130))  # Zmenšený rozestup
screen.blit(text6, (width // 2 - text6.get_width() // 2, height // 8 + 160))  # Zmenšený rozestup
screen.blit(text7, (width // 2 - text7.get_width() // 2, height // 8 + 190))  # Zmenšený rozestup
screen.blit(text8, (width // 2 - text8.get_width() // 2, height // 8 + 220))  # Zmenšený rozestup
screen.blit(text9, (width // 2 - text9.get_width() // 2, height // 8 + 250))  # Zmenšený rozestup
screen.blit(text10, (width // 2 - text10.get_width() // 2, height // 8 + 280))  # Zmenšený rozestup

pygame.display.update()  # Aktualizace obrazovky

# Čekání na stisknutí Enter
waiting_for_enter = True  # Flag pro čekání na stisknutí Enter
while waiting_for_enter:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Ukončení programu
            pygame.quit()
            sys.exit(0)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            waiting_for_enter = False  # Pokračujeme do samotné hry

# ----------------- Konec přidané úvodní obrazovky -----------------

# Po stisknutí Enter se nastartuje samotná hra s černým pozadím
screen.fill(black)  # Nastavení černé obrazovky pro samotnou hru
pygame.display.update()  # Aktualizace obrazovky

# Hlavní herní smyčka
while True: 
    for event in pygame.event.get():  # Prochází všechny události
        if event.type == pygame.QUIT:  # Pokud je událost typu "QUIT" (například zavření okna)
            pygame.quit()  # Ukončí Pygame, ukončí všechny Pygame funkce a zavře okno
            sys.exit(0)  # Ukončí Python program

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse // (margin + size_block)
            row = y_mouse // (margin + size_block)
            
            # střídání hráčů
            if mas[row][col] == 0:
                if query % 2 == 0:
                    mas[row][col] = 'x'
                else: 
                    mas[row][col] = 'o'
                query += 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_over = False
            mas = [[0] * 3 for i in range(3)]
            query = 0
            screen.fill(black)

    for row in range(3):
        for col in range(3):
            if mas[row][col] == "x":
                color = red
            elif mas[row][col] == 'o':
                color = green
            else: 
                color = white
            x = col * size_block + (col + 1) * margin
            y = row * size_block + (row + 1) * margin
            pygame.draw.rect(screen, color, (x, y, size_block, size_block))
            if color == red:
                pygame.draw.line(screen, white, (x + 5, y + 5), (x + size_block - 5, y + size_block - 5), 5)
                pygame.draw.line(screen, white, (x + size_block - 5, y + 5), (x + 5, y + size_block - 5), 5)
            elif color == green:
                pygame.draw.circle(screen, white, (x + size_block // 2, y + size_block // 2), size_block // 2 - 3, 5)
    
    if (query - 1) % 2 == 0:
        game_over = check_win(mas, "x")
    else:
        game_over = check_win(mas, "o")
    
    if game_over:
        screen.fill(black)  # Obrazovka bude celá černá
        font = pygame.font.SysFont('stxingkai', 80)  # Vytvoření písma
        text1 = font.render(game_over, True, white)
        text_rect = text1.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2  # Centrum 
        text_y = screen.get_height() / 2 - text_rect.height / 2  # Centrum
        screen.blit(text1, [text_x, text_y])
    
    pygame.display.update()

