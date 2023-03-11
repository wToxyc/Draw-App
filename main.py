import pygame, sys, os

pygame.init()

white_color = pygame.Color(255, 255, 255)
black_color = pygame.Color(0, 0, 0)
grey_color = pygame.Color(80, 80, 80)
red_color = pygame.Color(255, 0, 0)
green_color = pygame.Color(0, 255, 0)
blue_color = pygame.Color(0, 0, 255)

window = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Draw App")
window.fill(white_color)

next = True
line_beginning = 0, 0
color = black_color
thickness = 1

while next:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            next = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                next = False
            elif event.key == pygame.K_r:
                color = red_color
            elif event.key == pygame.K_g:
                color = green_color
            elif event.key == pygame.K_b:
                color = blue_color
            elif event.key == pygame.K_n:
                color = black_color
            elif event.key == pygame.K_c:
                color = white_color
            elif event.key == pygame.K_s:
                if not os.path.exists("img/"):
                    os.mkdir("img")
                i = 1
                while os.path.exists(f"img/draw{i}.png"):
                    i += 1
                pygame.image.save(window, f"img/draw{i}.png")
            elif event.key == pygame.K_o:
                window.blit(pygame.image.load().convert(), (0, 0))
            elif event.key == pygame.K_DELETE:
                window.fill(white_color)
        elif event.type == pygame.MOUSEMOTION:
            line_end = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed() == (1, 0, 0):
                pygame.draw.line(window, color, line_beginning, line_end, thickness) 
            elif pygame.mouse.get_pressed() == (0, 0, 1):
                pygame.draw.line(window, white_color, line_beginning, line_end, thickness)
            line_beginning = line_end
        elif event.type == pygame.MOUSEWHEEL:
            if event.y == 1:
                thickness += 1
            else:
                if thickness == 1:
                    continue
                thickness -= 1

    pygame.display.flip()