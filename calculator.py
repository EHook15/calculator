import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption('Calculator')

buttoncolor = (230, 230, 230)
buttoncolor2 = (200, 200, 200)

font = pygame.font.Font(None, 40)
font2 = pygame.font.Font(None, 30)

def drawbutton(text, x, y, w, h, color):
    pygame.draw.rect(screen, color, (x, y, w, h), 0)
    pygame.draw.rect(screen, (0, 0, 0), (x, y, w, h), 3)
    label = font.render(text, True, (0, 0, 0))
    screen.blit(label, (x + w // 2 - label.get_width() // 2, y + h // 2 - label.get_height() // 2))

def display_text(expression):
    text = font.render(expression, True, (0, 0, 0))
    screen.blit(text, (20, 20))

def calculator():
    expression = ""
    result = ""
    running = True
    while running:
        screen.fill((255, 255, 255))
        
        display_text(expression)

        buttons = [
            ('7', 20, 100),
            ('8', 100, 100),
            ('9', 180, 100),
            ('/', 260, 100),
            ('4', 20, 180),
            ('5', 100, 180),
            ('6', 180, 180),
            ('*', 260, 180),
            ('1', 20, 260),
            ('2', 100, 260),
            ('3', 180, 260),
            ('-', 260, 260),
            ('0', 20, 340),
            ('.', 100, 340),
            ('+', 180, 340),
            ('=', 260, 340),
            ('C', 20, 420)
        ]

        for (text, x, y) in buttons:
            drawbutton(text, x, y, 60, 60, buttoncolor)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if 20 <= mouse_x <= 80 and 100 <= mouse_y <= 160:      # 7 
                    expression += '7'
                elif 100 <= mouse_x <= 160 and 100 <= mouse_y <= 160:  # 8 
                    expression += '8'
                elif 180 <= mouse_x <= 240 and 100 <= mouse_y <= 160:  # 9 
                    expression += '9'
                elif 260 <= mouse_x <= 320 and 100 <= mouse_y <= 160:  # / 
                    expression += '/'
                elif 20 <= mouse_x <= 80 and 180 <= mouse_y <= 240:    # 4 
                    expression += '4'
                elif 100 <= mouse_x <= 160 and 180 <= mouse_y <= 240:  # 5 
                    expression += '5'
                elif 180 <= mouse_x <= 240 and 180 <= mouse_y <= 240:  # 6 
                    expression += '6'
                elif 260 <= mouse_x <= 320 and 180 <= mouse_y <= 240:  # * 
                    expression += '*'
                elif 20 <= mouse_x <= 80 and 260 <= mouse_y <= 320:    # 1 
                    expression += '1'
                elif 100 <= mouse_x <= 160 and 260 <= mouse_y <= 320:  # 2 
                    expression += '2'
                elif 180 <= mouse_x <= 240 and 260 <= mouse_y <= 320:  # 3 
                    expression += '3'
                elif 260 <= mouse_x <= 320 and 260 <= mouse_y <= 320:  # - 
                    expression += '-'
                elif 20 <= mouse_x <= 80 and 340 <= mouse_y <= 400:    # 0 
                    expression += '0'
                elif 100 <= mouse_x <= 160 and 340 <= mouse_y <= 400:  # . 
                    expression += '.'
                elif 180 <= mouse_x <= 240 and 340 <= mouse_y <= 400:  # + 
                    expression += '+'
                elif 260 <= mouse_x <= 320 and 340 <= mouse_y <= 400:  # = 
                    try:
                        result = str(eval(expression))
                        expression = result
                    except:
                        result = "Error"
                        expression = ""
                elif 20 <= mouse_x <= 80 and 420 <= mouse_y <= 480:    # C 
                    expression = ""

        pygame.display.update()

calculator()

pygame.quit()
sys.exit()
