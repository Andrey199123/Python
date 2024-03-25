import pygame

# initialize
pygame.init()
screen = pygame.display.set_mode((1000, 618))
# Caption
pygame.display.set_caption("Earth")
# Clock
clock = pygame.time.Clock()
# Surface
surface = pygame.Surface((500, 309))
surface.fill("wheat3")


# Functions and classes
class Go_around:
    def __init__(self, image, rect):
        self.original_image = image
        self.image = self.original_image.copy()
        self.rect = image.get_rect(topleft=rect.midbottom)
        self.last_rotation = pygame.time.get_ticks()
        self.rotation_degree = 0
        self.rotation_speed = 3
        self.bottom = True
        self.left = False
        self.rotate_class = False
        self.rotate_bottomleft = True
        self.top = False
        self.rotate_topleft = False
        self.right = False
        self.rotate_bottomright = False
        self.rotate_topright = False

    def rotate(self):
        """Rotates each car around its center around the rectangle"""
        if self.rotation_degree > 360:
            self.rotation_degree = 0
        current_time = pygame.time.get_ticks()
        if current_time - self.last_rotation > 1 and self.rotate_class == True:
            self.last_rotation = current_time
            # Since we are actually rotating the original image from its horizontal position and not the new image each time, we need to rotate it by an increasingly larger amount each time
            self.rotation_degree += self.rotation_speed
            self.image = pygame.transform.rotate(self.original_image, -1 * self.rotation_degree)

    def square(self):
        """Logic for each car to go around the rectangle"""
        if self.bottom:
            self.rect.left -= 5
        if self.rect.right < wall_rect.left and self.rotate_bottomleft:
            self.bottom, self.rotate_class = False, True
            self.rotate()
        if self.rect.bottom < 154 and self.left == False:
            self.left, self.rotate_topleft = True, True
        if self.rotate_topleft:
            self.rotate_class = True
            self.rotate()
        if self.rect.left > 750 and self.top == False:
            self.rotate_topright, self.top = True, True
        if self.rotate_topright:
            self.rotate_class = True
            self.rotate()
        if self.right:
            self.rect.bottom += 5
        if self.rect.top > 463 and self.right:
            self.rotate_bottomright, self.right = True, False
        if self.rotate_bottomright:
            self.rotate_class = True
            self.rotate()
        # Rotations
        if self.rotation_degree >= 360 and self.rotate_bottomright == True:
            self.rotate_bottomright, self.rotate_class, self.bottom, self.left, self.rotate_bottomleft, self.top, self.rotate_topleft, self.rotate_topright, self.right = False, False, True, False, True, False, False, False, False
        elif self.rotation_degree % 360 >= 270 and self.rotate_topright == True:
            self.rotate_class, self.rotate_topright, self.right = False, False, True
        elif self.rotation_degree % 360 >= 180 and self.top == False:
            self.rotate_class, self.rotate_topleft = False, False
            self.rect.left += 5
        elif self.rotation_degree % 360 >= 90 and self.left == False:
            self.rect.top -= 5
            self.rotate_class, self.rotate_bottomleft = False, False

    def update(self):
        screen.blit(self.image, self.rect)


wall = pygame.image.load("stone_wall.png").convert_alpha()
wall_rect = wall.get_rect(topleft=(275, 250))
# Cars
car = pygame.image.load("image.png").convert_alpha()
car_rect = car.get_rect(topleft=(-400, 200))
mercedes = pygame.image.load("Mercedes.png").convert_alpha()
mercedes = pygame.transform.rotozoom(mercedes, 0, 0.2)
mercedes.set_colorkey((205, 201, 201))
bugatti = pygame.image.load("Bugatti.png").convert_alpha()
bugatti = pygame.transform.rotozoom(bugatti, 0, 0.24)
bugatti.set_colorkey((205, 201, 201))
ferrari = pygame.image.load("Ferrari.png").convert_alpha()
ferrari = pygame.transform.rotozoom(ferrari, 0, 0.23)
ferrari.set_colorkey((205, 201, 201))
# Variables
go, y, wall_length, mercedes_class, mercedes_loop, spawn_timer, obj_list, car_list, car_loop = True, False, wall_rect.bottom - wall_rect.top, Go_around(
    mercedes, wall_rect), 1, pygame.USEREVENT + 1, [], [mercedes, ferrari, bugatti], 0
pygame.time.set_timer(spawn_timer, 3000)
for i in range(20):
    globals()[f"mercedes{i}"] = Go_around(car_list[car_loop % 3], wall_rect)
    car_loop += 1
globalss = [name for name in globals()]
print(str(len(globalss)) + " variables")
while True:
    time = pygame.time.get_ticks()
    mouse = pygame.mouse.get_pos()
    screen.fill((205, 201, 201))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # Mercedes
        if event.type == spawn_timer:
            globals()[f"mercedes{mercedes_loop}"].square()
            obj_list.append(globals()[f"mercedes{mercedes_loop}"])
            mercedes_loop += 1
    for value in obj_list:
        value.square()
    mercedes_class.square()
    # car
    if go:
        car_rect.left += 5
    else:
        car_rect.left -= 5
    if car_rect.left > 1000:
        go = False
    elif car_rect.left < -400:
        go = True
    if car_rect.colliderect(wall_rect):
        car_rect.top -= wall_length
    if car_rect.colliderect(wall_rect) and car_rect.right > wall_rect.right and y == False:
        car_rect.top -= wall_length
        y = True
    if car_rect.colliderect(wall_rect) == False and car_rect.bottom <= wall_rect.top:
        if car_rect.right < wall_rect.left:
            car_rect.top += wall_length
        elif car_rect.left > wall_rect.right:
            car_rect.top += wall_length
    # Make everything show up on surface
    mercedes_class.update()
    for value in obj_list:
        value.update()
    screen.blit(surface, (250, 154))
    screen.blit(car, car_rect)
    screen.blit(wall, wall_rect)
    pygame.display.update()
    clock.tick(30)
