import pygame
import random
import csv

WIDTH = 800
HEIGHT = 800
FPS = 30

#fancy colors
BLACK = (29,30,34)
WHITE = (255,255,255)
BLUE = (58,70,96)
YELLOW = (254,218,106)
SILVER = (212,212,220)
GREY = (57,63,77)


button_list = []

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

class Infobox(pygame.sprite.Sprite):
    def __init__(self,current_number,current_id):
        super().__init__()

        #i_text = "{} {}".format(current_number,current_id)

        self.image = pygame.Surface((100,100))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()

        self.rect.x = 500
        self.rect.y = 500

        self.font = pygame.font.SysFont("Consolas", 20)
        self.textSurf = self.font.render(current_number, 50, WHITE)

        # t_width = self.textSurf.get_width()
        # t_height = self.textSurf.get_height()
        self.textrect = self.textSurf.get_rect(center=self.image.get_rect().center)

        self.image.blit(self.textSurf, self.textrect)

class Wordbox(pygame.sprite.Sprite):
    def __init__(self,t_text, t_color, t_width, t_height,x_pos,y_pos):
        super().__init__()

        self.image = pygame.Surface([t_width,t_height])
        self.image.fill(GREY)
        self.rect = self.image.get_rect()

        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect.x = self.x_pos
        self.rect.y = self.y_pos

        self.font = pygame.font.SysFont("Consolas", 20)
        self.textSurf = self.font.render(t_text, 50, t_color)

        # t_width = self.textSurf.get_width()
        # t_height = self.textSurf.get_height()
        self.textrect = self.textSurf.get_rect(center=self.image.get_rect().center)

        self.image.blit(self.textSurf, self.textrect)

        button_list.append(pygame.Rect(x_pos, y_pos, t_width, t_height))

#import text
term_array = []
with open('descriptions801-1200.csv') as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        term_array.append(row)

current_number = term_array[0][0]
current_id =  term_array[0][1]
current_desc = term_array[0][3]

temp_array = []
final_array = []
string = []
ss = current_desc.split()

# create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((HEIGHT,WIDTH))
pygame.display.set_caption("VG")
clock = pygame.time.Clock()

#create sprites
all_sprites = pygame.sprite.Group()
all_info = pygame.sprite.Group()

tot_w_len = 20
y_pos = 50
x_pos = 20

for i in range(len(ss)):
    if x_pos > WIDTH - 200:
        y_pos += 40
        tot_w_len = 0
        x_pos = 20
    x_pos = tot_w_len
    w_len = len(ss[i]) * 12
    tot_w_len = tot_w_len+ w_len + 20
    wordbox = Wordbox(ss[i],WHITE,w_len,25,x_pos,y_pos)
    all_sprites.add(wordbox)
    infobox = Infobox(current_id,current_number)
    all_info.add(infobox)

# game loop
running = True
while running:
    #loop speed
    clock.tick(FPS)
    #process input
    # for event in pygame.event.get():
        #check for closing window
    event = pygame.event.poll()

    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
        x,y = event.pos
        for i in range(len(button_list)):
            if x > button_list[i].left and x < button_list[i].right and y > button_list[i].top and y <  button_list[i].bottom:
                all_sprites.sprites()[i].image.fill(SILVER)
                all_sprites.sprites()[i].image.blit(all_sprites.sprites()[i].textSurf, all_sprites.sprites()[i].textrect)
                temp_array.append(ss[i])
    if event.type == pygame.KEYUP and event.key == pygame.K_LSHIFT:

        string.append(" ".join(temp_array))
        final_array.append(string)
        temp_array = []
        string = []

    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        # Set the x, y postions of the mouse click
        x, y = event.pos
        print("left click only")

        for i in range(len(button_list)):
            if x > button_list[i].left and x < button_list[i].right and y > button_list[i].top and y <  button_list[i].bottom:
                all_sprites.sprites()[i].image.fill(YELLOW)
                all_sprites.sprites()[i].image.blit(all_sprites.sprites()[i].textSurf, all_sprites.sprites()[i].textrect)
                temp_array.append(ss[i])
                print("added: {}".format(ss[i]))
                final_array.append(temp_array)
                temp_array = []

    elif event.type == pygame.QUIT:
        running = False

    #update
    all_sprites.update()
    #draw
    screen.fill(BLACK)
    all_sprites.draw(screen)
    all_info.draw(screen)

    pygame.display.flip()

print(final_array)
fname = "C:/Users/User/Desktop/fff.csv"
listFile2 = open('C:/Users/User/Desktop/fff.csv', 'w')
writer2 = csv.writer(listFile2,lineterminator = '\n')
for item in final_array:
    writer2.writerow(item)
pygame.quit()
