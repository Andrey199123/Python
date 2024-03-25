import pygame as pg
from sys import exit
import time
start = time.perf_counter()
pg.init()
screen = pg.display.set_mode((1860, 1150))
screen.fill("white")
pg.display.set_caption("Fonts")
fonts, clock, color1, color2, color3 = ["Lato-Black.ttf", "Midnight.otf", "ZakirahsHand.ttf",
                                        "zagreb_underground.ttf",
                                        "Zag Regular.otf",
                                        "Zado.ttf",
                                        "gomarice_font_yaki_goma 2.ttf",
                                        "yayusa.ttf",
                                        "qikicons real estate.otf",
                                        "X-PRISM.ttf"], pg.time.Clock(), 255, 255, 255
start_typing, make_sure, user_text, type_y, type_x, font_for_typing, once_list, color_type, color_type2, color_type3, collide_list = False, False, "a", 0, 925, 0, [], False, False, False, []
print("Click on a font to type with, then press any key to start typing.")


def return_function(x_function, y_function):
    y_function += once_list[0] + 10
    x_function = 925
    return x_function, y_function


pg.key.set_repeat(200)
finish = time.perf_counter()
#print(f"Finished in {round(finish-start, 2)} seconds")
while True:
    keys = pg.key.get_pressed()
    for event in pg.event.get():
        mouse = pg.mouse.get_pos()
        mouse_x, mouse_y = pg.mouse.get_pos()
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == pg.K_RETURN:
            type_x = return_function(type_x - 10, type_y)[0]
            type_y += once_list[0] + 10
        # delete function, also deletes part under character
        if event.type == pg.K_BACKSPACE:
            type_x -= once_list[0]
            screen.fill("white", rect=[type_x, type_y, once_list[0], 16 / 9 * once_list[0]])
        if event.type == pg.KEYDOWN and start_typing:
            type_size = int(input("Choose the size you will type in."))
            once_list.append(type_size)
            type_color = str(input("Choose the color you will type in."))
            type_location = input("Will you type at the top, center, or bottom?")
            if type_location == "top":
                type_y = 75
            elif type_location == "center":
                type_y = 450
            else:
                type_y = 700
            print("You can now type.")
            start_typing = False
            make_sure = True
        if event.type == pg.KEYDOWN and make_sure:
            user_text = event.unicode
            type_font = pg.font.Font(fonts[font_for_typing], type_size)
            type_surface = type_font.render(str(user_text[0]), True, type_color)
            screen.blit(type_surface, (type_x, type_y))
            type_x += int(type_size)
    x, y = 0, 30
    if color1 < 175:
        color_type, color_type2, color_type3 = False, True, True
    if color1 >= 235 and color_type3:
        color1, color2, color3 = 255, 255, 255
        color_type3, color_type2 = False, False
    if color_type:
        color1 -= 20
        color2 -= 20
        color3 -= 20
    if color_type2:
        color1 += 40
        color2 += 40
        color3 += 40
    try:
        variablesa = pg.font.Font(fonts[collide_list[0]], 30)
        variables2a = variablesa.render(fonts[collide_list[0]], True, "black")
        variables3a = variables2a.get_rect(topleft=(30, y))
        pg.draw.rect(screen, (color1, color2, color3), (30, collide_list[1], variables3a[2], variables3a[3]))
    except:
        pass
    for value in fonts:
        variables = pg.font.Font(fonts[x], 30)
        variables2 = variables.render(fonts[x], True, "black")
        variables3 = variables2.get_rect(topleft=(30, y))
        screen.blit(variables2, (30, y))
        if variables3.collidepoint(mouse) and event.type == pg.MOUSEBUTTONDOWN:
            collide_list.clear()
            collide_list.append(x)
            collide_list.append(y)
            color_type = True
            font_for_typing = x
            start_typing = True
        x += 1
        y += 60
    if type_x >= 1800:
        type_x, type_y = return_function(type_x, type_y)[0], return_function(type_x, type_y)[1]
    if type_x < 925:
        # (1800-925) Remainder type_size
        type_x = 1800 + (875 % once_list[0])
        type_y -= once_list[0] + 10
    pg.display.update()
    clock.tick(40)
