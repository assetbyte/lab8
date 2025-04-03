import pygame

pygame.init()


WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")


colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  
current_color = colors[0]  
draw_mode = "brush"  


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                current_color = colors[0]  
            elif event.key == pygame.K_2:
                current_color = colors[1]  
            elif event.key == pygame.K_3:
                current_color = colors[2]
            elif event.key == pygame.K_r:
                draw_mode = "rect" 
            elif event.key == pygame.K_c:
                draw_mode = "circle"  

    
    if pygame.mouse.get_pressed()[0]: 
        x, y = pygame.mouse.get_pos()
        if draw_mode == "brush":
            pygame.draw.circle(screen, current_color, (x, y), 5)
        elif draw_mode == "circle":
            pygame.draw.circle(screen, current_color, (x, y), 30, 2)
        elif draw_mode == "rect":
            pygame.draw.rect(screen, current_color, (x - 15, y - 15, 30, 30), 2)

    elif pygame.mouse.get_pressed()[2]: 
        x, y = pygame.mouse.get_pos()
        pygame.draw.circle(screen, "black", (x, y), 20)

    pygame.display.update()

pygame.quit()
