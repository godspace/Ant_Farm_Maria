import pygame

# Initialize Pygame
pygame.init()

font1 = pygame.font.SysFont("Arial", 25)
font1.set_bold(True)

# Window dimensions
width = 800
height = 600

# Create the window
window = pygame.display.set_mode((width, height))

# Window title
pygame.display.set_caption("My Game")

# Upload bg
fon_01 = pygame.transform.scale(pygame.image.load(r'images\Fon1.jpg'), (width, height))
fon_02 = pygame.transform.scale(pygame.image.load(r'images\Fon2.jpeg'), (width, height))
fon_03 = pygame.transform.scale(pygame.image.load(r'images\Fon3.jpg'), (width, height))
fon_04 = pygame.transform.scale(pygame.image.load(r'images\Fon4.jpg'), (width, height))
upgreat_01 = pygame.transform.scale(pygame.image.load(r'images\upgreat_1.jpg'), (width, height))
upgreat_02 = pygame.transform.scale(pygame.image.load(r'images\upgreat_2.jpg'), (width, height))
upgreatlist = [fon_02, upgreat_01, upgreat_02]

current_fon = fon_01

#Upload buttons
b0 = pygame.transform.scale(pygame.image.load(r'images\start_button.png'), (100, 100))
b1 = pygame.transform.scale(pygame.image.load(r'images\queen_button.png'), (100, 100))
b2 = pygame.transform.scale(pygame.image.load(r'images\workers_button.png'), (100, 100))
b3 = pygame.transform.scale(pygame.image.load(r'images\defenders_button.png'), (100, 100))
b4 = pygame.transform.scale(pygame.image.load(r'images\feed_queen_button.png'), (100, 100))
b5 = pygame.transform.scale(pygame.image.load(r'images\upgrade_button.png'), (100, 100))
b6 = pygame.transform.scale(pygame.image.load(r'images\buy_worker_button.png'), (100, 100))
b7 = pygame.transform.scale(pygame.image.load(r'images\main_menu.png'), (100, 100))



class Button:
    def __init__(self, x,y, image):
        self.image = image
        self.hitbox = image.get_rect(center = (x, y))
        self.image.set_alpha(255)
        self.enable = True
    
    def click(self):
        if self.enable:
            if pygame.mouse.get_pressed()[0]:
                if self.hitbox.collidepoint(pygame.mouse.get_pos()):
                    return True
    
    def make_invisible(self):
        self.image.set_alpha(0)
        self.enable = False
    
    def make_visible(self):
        self.image.set_alpha(255)
        self.enable = True

start_btn = Button(width//2, height//2, b0)

qeen_btn = Button(width//2, height//3, b1)
qeen_btn.make_invisible()

worker_btn = Button(width//3, height//3, b2)
worker_btn.make_invisible()

guard_btn = Button(width//1.5, height//3, b3)
guard_btn.make_invisible()

menu_btn = Button(width//2, height - 100, b7)
menu_btn.make_invisible()

feed_btn = Button(width//3, height//2, b4)
feed_btn.make_invisible()

upgreat_btn = Button(width//1.5, height//2, b5)
upgreat_btn.make_invisible()

buy_worker_btn = Button(width//2, height//2, b6)
buy_worker_btn.make_invisible()

buttons_list = [start_btn, qeen_btn, worker_btn, guard_btn, menu_btn, feed_btn, upgreat_btn, buy_worker_btn]

class Qeen():
    def __init__(self) -> None:
        self.food = 100
        self.upgreat = 0
        self.upgreat_price = 10
        self.speed = 1

class Worker():
    def __init__(self) -> None:
        self.ammount = 0
        self.food = 0
        self.speed = 0.1
        self.price = 3

qeen = Qeen()
worker = Worker()

pygame.time.set_timer(pygame.USEREVENT, 1000)

def open_start_menu():
    global current_fon
    current_fon = upgreatlist[qeen.upgreat]
    start_btn.make_invisible()
    feed_btn.make_invisible()
    upgreat_btn.make_invisible()
    buy_worker_btn.make_invisible()
    qeen_btn.make_visible()
    worker_btn.make_visible()
    guard_btn.make_visible()

def open_qeen_menu():
    global current_fon
    current_fon = fon_03
    qeen_btn.make_invisible()
    worker_btn.make_invisible()
    guard_btn.make_invisible()
    menu_btn.make_visible()
    feed_btn.make_visible()
    upgreat_btn.make_visible()

def open_worker_menu():
    global current_fon
    current_fon = fon_04
    qeen_btn.make_invisible()
    worker_btn.make_invisible()
    guard_btn.make_invisible()
    menu_btn.make_visible()
    buy_worker_btn.make_visible()


def show_indicators():
    qeen_food_img = font1.render(str(qeen.food), True, (255,0,0))
    window.blit(qeen_food_img, (0,0))
    worker_food_img = font1.render(str(round(worker.food,1)), True, (255,0,0))
    window.blit(worker_food_img, (100,0))
    worker_ammount_img = font1.render(str(worker.ammount), True, (255,0,0))
    window.blit(worker_ammount_img, (200,0))

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if feed_btn.click():
                if worker.food >= qeen.speed:
                    qeen.food += qeen.speed
                    worker.food -= qeen.speed
            elif buy_worker_btn.click():
                if qeen.food >= worker.price:
                    worker.ammount += 1
                    qeen.food -= worker.price
            elif upgreat_btn.click():
                if qeen.food >= qeen.upgreat_price:
                    qeen.upgreat += 1
                    qeen.food -= qeen.upgreat_price
                    worker.speed *= 10
                    qeen.upgreat_price *= 10
                    qeen.speed *= 10
        elif event.type == pygame.USEREVENT:
            qeen.food -= 1
            worker.food += worker.speed * worker.ammount

    window.blit(current_fon,(0,0))

    for button in buttons_list:
        window.blit(button.image, button.hitbox)
    
    if start_btn.click():
        open_start_menu()
    if qeen_btn.click():
        open_qeen_menu()
    if menu_btn.click():
        open_start_menu()
    if worker_btn.click():
        open_worker_menu()

    show_indicators()
    # Add game rendering code here

    # Update the screen
    pygame.display.update()

# Quit the program
pygame.quit()