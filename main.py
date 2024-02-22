import pygame
import math
import sys
import game

#try and add title look at line 14 onwards DONE
#try and make prettier - import image in pygame window, colours DONE
#sys: The sys module in Python provides various functions and variables that are used to manipulate different parts of the Python runtime environment. DONE
#try and do rules page - unsure how to format text on different lines DONE



def end():
    screen.fill(dark_blue)
    game_font = pygame.font.SysFont("Andale Mono", 60)
    game_text = game_font.render("Thank you for playing!", True, (255,255,255))
    game_rect = game_text.get_rect(center = (width//2, height//2))
    screen.blit(game_text, game_rect)

    pygame.display.update()
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()

def playGame():
    game.main()


class Button:
    def __init__(self, button_name, x, y, action):
        self.rect = pygame.rect.Rect(x, y, 200, 50)
        self.button_name = button_name
        self.action = action

    def draw(self):
        pygame.draw.rect(screen, light_purple, self.rect)
        pygame.draw.rect(screen, (255,255,255), self.rect, 2)
        text_surface = menu_font.render(self.button_name, True, (255,255,255))
        text_rect = text_surface.get_rect(center = self.rect.center)
        screen.blit(text_surface, text_rect)


pygame.init()
width = 1000
height = 600
white = (255,255,255)
blue = (102, 158, 204)
light_blue = (179, 207, 230)
dark_blue = (49, 44, 145)
light_purple = (88, 83, 173)
menu_font = pygame.font.Font(None, 35)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Praddy's Peculiar Penguins...")

penguin = pygame.image.load("penguin.png").convert()



def rules():
    screen.fill(dark_blue)
    game_font1 = pygame.font.SysFont("Andale Mono", 30)
    game_font2 = pygame.font.SysFont("Andale Mono", 20)

    title_text = "Rules"
    rules_text = [
        "AIM: Try to hit the launch target by varying launch angle and speed.",
        "SCORING: 5 points for every bullseye, 1 point if the penguin lands on the target.",
        "Good Luck!!!"
    ]

    title_render = game_font1.render(title_text, True, white)
    rules_render = [game_font2.render(rule, True, white) for rule in rules_text]

    title_rect = title_render.get_rect(center=[width // 2, 120])
    rules_rect = [rule.get_rect(center=[width // 2, 200 + i * 70]) for i, rule in enumerate(rules_render)]

    screen.blit(title_render, title_rect)
    for rule_render, rule_rect in zip(rules_render, rules_rect):
        screen.blit(rule_render, rule_rect)

    iceberg = pygame.image.load("icebergs.png").convert()
    imageSize = (1000, 200)
    iceberg = pygame.transform.scale(iceberg, imageSize)
    screen.blit(iceberg, (0, height - 200))
    
    
    start_button = Button("Back", 70, 500, None)
    start_button.draw()  # Corrected line
    pygame.display.flip()
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if start_button.rect.collidepoint(event.pos):   
                        return 
        pygame.display.flip()
        pygame.time.Clock().tick(30)





start_button = Button("Start", ((width//2)-100) , 210, playGame)
rules_button = Button("Rules", ((width//2)-100), 280, rules)
leaderboard_button = Button("Leaderboard", ((width//2)-100), 350, None)
end_button = Button("End", ((width//2)-100), 420, end)


buttons = [start_button, rules_button, leaderboard_button, end_button]

running = True



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: #left click
                for button in buttons:
                    if button.rect.collidepoint(event.pos):
                        button.action()
    screen.fill(dark_blue)

    game_font = pygame.font.SysFont("Andale Mono", 50)
    game_text = game_font.render("Praddy's Peculiar Penguins", True, (255,255,255))
    game_rect = game_text.get_rect(center = (width//2, 140))
    screen.blit(game_text, game_rect)

    for button in buttons:
        button.draw()

    screen.blit(penguin,(width-200,height-200))
    imageSize = (200,200)
    penguin = pygame.transform.scale(penguin,imageSize)
    pygame.display.flip()

    

    pygame.display.update()






# DISPLAY = pygame.display.set_mode((1000,600))
# pygame.display.set_caption("Praddy's Peculiar Penguins...")
# pygame.display.update()

# cannon = pygame.image.load("/Users/pradeeshanna/Documents/computing/Peculiar penguins/cannon2.png").convert()
# DISPLAY.blit(cannon,(0,0))
# imageSize = (200,200)
# cannon = pygame.transform.scale(cannon,imageSize)
# pygame.display.flip()

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False



