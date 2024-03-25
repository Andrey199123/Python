import pygame as pg
from sys import exit
import random
import sqlite3
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
from stopwatch import Stopwatch


# Functions

def area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1)
                + x3 * (y1 - y2)) / 2.0)


def time():
    time_font = pg.font.Font(None, 25)
    time_render2 = time_font.render(f"{round((pg.time.get_ticks() - start_time) / 100) / 10}", True, (64, 64, 64))
    screen.blit(time_render2, (0, 0))


class Rotate(pg.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.orig_image = self.image
        self.rect = self.image.get_rect(topleft=(25, 5))
        self.angle = 0

    def update(self):
        self.angle -= 1
        self.rotate()

    def rotate(self):
        self.image = pg.transform.rotozoom(self.orig_image, self.angle, 1)
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect(center=self.rect.center)


class Login:
    # If a list were to be created here, it would be shared amongst all Login instances

    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("863x540+15+30")
        self.root.resizable(False, False)
        self.bg = ImageTk.PhotoImage(file="BMWM4CSL.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        self.frame2 = Frame(self.root, bg="#C09E7D")
        self.frame2.place(x=307, y=138, width=280, height=265)
        self.frame = Frame(self.root, bg="#9AAEBE")
        self.frame.place(x=312, y=143, width=270, height=255)
        self.user_txt = Label(self.frame, text="Username", font=("eurostile.TTF", 15, "bold"), fg="black",
                              bg="#9AAEBE").place(x=15, y=15)
        self.user = Entry(self.frame, font=("eurostile.TTF", 15, "bold"), bg="#C4D8E8")
        # Make sure to place separately for proper get() usage
        self.user.place(x=15, y=45)
        self.password_txt = Label(self.frame, text="Password", font=("eurostile.TTF", 15, "bold"), fg="black",
                                  bg="#9AAEBE").place(x=15, y=78)
        self.password = Entry(self.frame, show='*', font=("eurostile.TTF", 15, "bold"), bg="#C4D8E8")
        self.password.place(x=15, y=108)
        self.login = Button(self.frame, command=self.check_input, text="Login", bd=0,
                            font=("eurostile.TTF", 30, "bold"), bg="#C4D8E8", fg="#444A19").place(x=15, y=153)
        self.access = False
        self.register = Button(self.frame, command=self.register, text="Register", bd=0,
                               font=("eurostile.TTF", 30, "bold"), bg="#C4D8E8", fg="#444A19").place(x=115, y=153)
        self.del_acc = Button(self.frame, command=self.delete_account, text="Delete Account", bd=0,
                              font=("eurostile.TTF", 30, "bold"), bg="#C4D8E8", fg="#444A19").place(x=15, y=208)
        self.profile_user = self.user.get()
        self.user3 = None
        self.password3 = None
        self.name = None
        self.last = None
        self.birth = None
        self.user2 = None
        self.password2 = None
        self.root2 = None
        self.root3 = None
        self.conn = sqlite3.connect("passmanager.db")
        self.cursor = self.conn.cursor()
        conn = sqlite3.connect("passmanager.db")
        cursor = conn.cursor()
        cursor.execute(
            '''CREATE TABLE IF NOT EXISTS profile(First_Name text, Last_Name text, Birthdate text, Username text, Password text)''')
        conn.commit()
        cursor.execute("SELECT *, oid FROM profile")
        records = cursor.fetchall()
        self.p_records = ""
        for record in records:
            self.p_records += str(record[5]) + " " + str(record[0]) + " " + str(record[1]) + " " + str(
                record[2]) + " " + str(record[3]) + " " + str(record[4]) + "\n"
            # same thing as str(record[5]), str(record[0]), str(record[1]), str(record[2]), str(record[3]), str(record[4])
            self.records_list = [str(record[value % 6]) for value in range(5, 11)]
        print(self.p_records)
        conn.close()

    def check_input(self):
        if self.user.get() == "" or self.password.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.user.get() not in self.records_list or self.password.get() not in self.records_list or self.records_list.index(
                self.user.get()) + 1 != self.records_list.index(self.password.get()):
            messagebox.showerror("Error", "Incorrect username and/or password.", parent=self.root)
        else:
            messagebox.showinfo("Welcome", f"Welcome {self.user.get()}", parent=self.root)
            self.access = True
            self.conn.commit()
            self.conn.close()
            self.profile_user = self.user.get()

            try:
                self.root2.destroy()
                self.root3.destroy()
            except:
                pass
            root.destroy()

    def register(self):
        self.root2 = Toplevel(root)
        self.root2.title("Register")
        self.root2.resizable(False, False)
        self.root2.geometry("863x540+878+30")
        root2_bg = ImageTk.PhotoImage(file="Porsche911GT3.jpg")
        root2_bg_img = Label(self.root2, image=root2_bg).place(x=0, y=0, relwidth=1, relheight=1)
        register_frame2 = Frame(self.root2, bg="#C9C8C4")
        register_frame2.place(x=15, y=15, width=280, height=410)
        register_frame = Frame(self.root2, bg="#009AFC")
        register_frame.place(x=20, y=20, width=270, height=400)
        name_txt = Label(register_frame, text="First Name", font=("eurostile.TTF", 15, "bold"), fg="black",
                         bg="#009AFC").place(x=15, y=15)
        self.name = Entry(register_frame, font=("eurostile.TTF", 15, "bold"), bg="#0072D7")
        self.name.place(x=15, y=45)
        last_txt = Label(register_frame, text="Last Name", font=("eurostile.TTF", 15, "bold"), fg="black",
                         bg="#009AFC").place(x=15, y=80)
        self.last = Entry(register_frame, font=("eurostile.TTF", 15, "bold"), bg="#0072D7")
        self.last.place(x=15, y=110)
        birth_txt = Label(register_frame, text="Birthdate (MM/DD/YY)", font=("eurostile.TTF", 15, "bold"), fg="black",
                          bg="#009AFC").place(x=15, y=145)
        self.birth = Entry(register_frame, font=("eurostile.TTF", 15, "bold"), bg="#0072D7")
        self.birth.place(x=15, y=175)
        user2_txt = Label(register_frame, text="Username", font=("eurostile.TTF", 15, "bold"), fg="black",
                          bg="#009AFC").place(x=15, y=210)
        self.user2 = Entry(register_frame, font=("eurostile.TTF", 15, "bold"), bg="#0072D7")
        self.user2.place(x=15, y=240)
        password2_txt = Label(register_frame, text="Password", font=("eurostile.TTF", 15, "bold"), fg="black",
                              bg="#009AFC").place(x=15, y=275)
        self.password2 = Entry(register_frame, show='*', font=("eurostile.TTF", 15, "bold"), bg="#0072D7")
        self.password2.place(x=15, y=305)
        register_btn = Button(register_frame, command=self.check_input_register, text="Register", bd=0,
                              font=("eurostile.TTF", 30, "bold"), bg="#D7C100", fg="#444A19").place(x=15, y=345)
        self.root2.mainloop()

    def delete_account(self):
        self.root3 = Toplevel(root)
        self.root3.title("Delete Account")
        self.root3.resizable(False, False)
        self.root3.geometry("863x540+15+570")
        root3_bg = ImageTk.PhotoImage(file="MercedesAMGGT.jpg")
        root3_bg_img = Label(self.root3, image=root3_bg).place(x=0, y=0, relwidth=1, relheight=1)
        register_frame2_del = Frame(self.root3, bg="#73ACC1")
        register_frame2_del.place(x=15, y=15, width=280, height=260)
        register_frame_del = Frame(self.root3, bg="#FFD500")
        register_frame_del.place(x=20, y=20, width=270, height=250)
        del_acc_txt = Label(register_frame_del, text="Delete Account", font=("eurostile.TTF", 30, "bold"), fg="#444A19",
                            bg="#FFD500").place(x=15, y=15)
        user3_txt = Label(register_frame_del, text="Username", font=("eurostile.TTF", 15, "bold"), fg="black",
                          bg="#FFD500").place(x=15, y=60)
        self.user3 = Entry(register_frame_del, font=("eurostile.TTF", 15, "bold"), bg="#D7C100")
        self.user3.place(x=15, y=90)
        password3_txt = Label(register_frame_del, text="Password", font=("eurostile.TTF", 15, "bold"), fg="black",
                              bg="#FFD500").place(x=15, y=125)
        self.password3 = Entry(register_frame_del, show='*', font=("eurostile.TTF", 15, "bold"), bg="#D7C100")
        self.password3.place(x=15, y=155)
        del_acc = Button(register_frame_del, command=self.check_input_del_acc, text="Delete Account", bd=0,
                         font=("eurostile.TTF", 30, "bold"), bg="#D7C100", fg="#444A19").place(x=15, y=190)
        self.root3.mainloop()

    def check_input_register(self):
        check_date = str(self.birth.get())
        check_name = False
        check_last = False
        for value in self.name.get()[1:len(self.name.get())]:
            if value.isupper():
                check_name = True
        for value in self.last.get()[1:len(self.last.get())]:
            if value.isupper():
                check_last = True
        if self.user2.get() == "" or self.password2.get() == "" or self.name.get() == "" or self.last.get() == "" or self.birth.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root2)
        elif len(check_date) != 8 or check_date[2:3] != "/" or check_date[5:6] != "/" or check_date[
                                                                                         0:2].isalpha() or check_date[
                                                                                                           3:5].isalpha() or check_date[
                                                                                                                             6:8].isalpha() or int(
            check_date[0:2]) > 12 or int(check_date[0:2]) < 1 or int(check_date[3:5]) > 31 or int(check_date[3:5]) < 1:
            messagebox.showerror("Error", "Please enter a correct birthdate", parent=self.root2)
        elif self.name.get()[0].islower() or check_name:
            messagebox.showerror("Error", "Please enter a proper first name", parent=self.root2)
        elif self.last.get()[0].islower() or check_last:
            messagebox.showerror("Error", "Please enter a proper last name", parent=self.root2)
        else:
            messagebox.showinfo("Register Success", "Register Success", parent=self.root2)
            conn = sqlite3.connect("passmanager.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO profile VALUES (:First_Name, :Last_Name, :Birthdate, :Username, :Password)",
                           {
                               'First_Name': self.name.get(),
                               'Last_Name': self.last.get(),
                               'Birthdate': self.birth.get(),
                               'Username': self.user2.get(),
                               'Password': self.password2.get()
                           }
                           )
            conn.commit()
            cursor.execute("SELECT *, oid FROM profile")
            records = cursor.fetchall()
            self.p_records = ""
            self.records_list = []
            for record in records:
                self.p_records += str(record[5]) + " " + str(record[0]) + " " + str(record[1]) + " " + str(
                    record[2]) + " " + str(record[3]) + " " + str(record[4]) + "\n"
                self.records_list = [str(record[value % 6]) for value in range(5, 11)]
            print(self.p_records)
            conn.close()
            self.name.delete(0, END)
            self.last.delete(0, END)
            self.birth.delete(0, END)
            self.user2.delete(0, END)
            self.password2.delete(0, END)

    def check_input_del_acc(self):
        if self.user3.get() == "" or self.password3.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root3)
        elif self.user3.get() not in self.records_list or self.password3.get() not in self.records_list or self.records_list.index(
                self.user3.get()) + 1 != self.records_list.index(self.password3.get()):
            messagebox.showerror("Error", "Invalid username and/or password", parent=self.root3)
        else:
            messagebox.showinfo("Account Deleted", "Account Deleted", parent=self.root3)
            conn = sqlite3.connect("passmanager.db")
            cursor = conn.cursor()
            # Subtract 5 from index of account's password to get index of id
            print(str(self.records_list[self.records_list.index(self.password3.get()) - 5]))
            cursor.execute("DELETE FROM profile where oid = " + str(
                self.records_list[self.records_list.index(self.password3.get()) - 5]))
            conn.commit()
            conn.close()
            self.user3.delete(0, END)
            self.password3.delete(0, END)


# Setup
root = Tk()
login_class = Login(root)
root.mainloop()
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((1860, 1150))
clock = pg.time.Clock()
pg.display.set_caption("Cursor Game")
# Variables
center_x, center_y, width, triangle_1x, triangle_1y, triangle_size, circle_x, circle_y, radius, start_time = random.randint(
    450, 1460), random.randint(250, 790), random.randint(100, 500), random.randint(450, 1460), random.randint(250,
                                                                                                              790), random.randint(
    200, 500), random.randint(450, 1460), random.randint(250, 790), random.randint(50, 125), 0
length = round(width * 1.61)
object, collinear, slope = pg.Rect(center_x - length / 2, center_y - width / 2, length, width), 0, 0
arc_center_x, arc_center_y, arc_width, arc_length, start_angle, back = random.randint(0, 1460), random.randint(0,
                                                                                                               790), random.randint(
    100, 500), random.randint(100, 500), random.randint(0, 6279), pg.image.load("BlackBack.png").convert_alpha()
end_angle, real_centerx, real_centery, menu, menu_rect, back = random.randint(start_angle,
                                                                              6280), arc_center_x + arc_length / 2, arc_center_y + arc_width / 2, True, pg.Rect(
    0, 0, 324, 200), pg.transform.rotozoom(back, 0, 0.05)
menu_rect.center, profile_rect, profile_screen, back_rect, play = (930, 575), pg.Rect(35, 2, 80,
                                                                                      30), False, back.get_rect(
    topleft=(0, 0)), False
boy_img, deep_img, sundance_img, overclock_img, studies_img, ipod = pg.image.load(
    "boy_img.jpg").convert_alpha(), pg.image.load("deep_img.jpg").convert_alpha(), pg.image.load(
    "sundance_img.jpg").convert_alpha(), pg.image.load("overclock_img.jpg").convert_alpha(), pg.image.load(
    "studies_img.jpg").convert_alpha(), pg.image.load("ipod.png").convert_alpha()
boy_img, sundance_img, overclock_img, studies_img, deep_img = pg.transform.rotozoom(boy_img, 0,
                                                                                    0.18), pg.transform.rotozoom(
    sundance_img, 0, 0.18), pg.transform.rotozoom(overclock_img, 0, 0.18), pg.transform.rotozoom(studies_img, 0,
                                                                                                 0.18), pg.transform.rotozoom(
    deep_img, 0, 0.18)
ipod, rotation_degree, rotation_speed, music_list = pg.transform.rotozoom(ipod, 0, 0.5), 0, 3, {
    "HNNY&KOKO-boy.mp3": boy_img,
    "HotSince82-DeepVoices.mp3": deep_img,
    "Fade2End-Sundance.mp3": sundance_img,
    "S.Charles-OverclockExtended.mp3": overclock_img,
    "ChrisBrann-StudiesInForm.mp3": studies_img}
ipod_rect, rectangle_dragging, offset_x, offset_y, music_update, music_paused, increment, increment2, x, length_dict = ipod.get_rect(
    topleft=(1000, 500)), False, 0, 0, True, False, 0, 0, 0, {"HNNY&KOKO-boy.mp3": 415,
                                                              "HotSince82-DeepVoices.mp3": 256,
                                                              "Fade2End-Sundance.mp3": 460,
                                                              "S.Charles-OverclockExtended.mp3": 336,
                                                              "ChrisBrann-StudiesInForm.mp3": 363}
# Surfaces
ipod_surf = pg.Surface((168, 130))
arc_surf = pg.Surface((1860, 1150))
ipod_surf.set_colorkey((0, 0, 0))
ipod.set_colorkey((0, 0, 0))
pg.draw.arc(arc_surf, "chartreuse4", (0, 0, arc_length, arc_width), start_angle / 1000, end_angle / 1000, width=5)
arc_mask = pg.mask.from_surface(arc_surf)
arc_surf.set_colorkey((0, 0, 0))
player_surf = pg.Surface((2, 2))
player_surf.fill("black")
player_rect = player_surf.get_rect(center=(0, 0))
player_mask = pg.mask.from_surface(player_surf)
circle_surf = pg.Surface((1860, 1150))
pg.draw.circle(circle_surf, "chartreuse4", (circle_x, circle_y), radius)
pg.draw.circle(circle_surf, "cornflowerblue", (circle_x, circle_y), radius, width=5)
circle_mask = pg.mask.from_surface(circle_surf)
circle_surf.set_colorkey((0, 0, 0))
ellipse_surf = pg.Surface((1860, 1150))
pg.draw.ellipse(ellipse_surf, "chartreuse4", object)
pg.draw.ellipse(ellipse_surf, "cornflowerblue", object, width=5)
ellipse_mask = pg.mask.from_surface(ellipse_surf)
ellipse_surf.set_colorkey((0, 0, 0))
# loops
while collinear == 0:
    triangle_2x, triangle_2y = random.randint(triangle_1x - triangle_size,
                                              triangle_1x + triangle_size), random.randint(
        triangle_1y - triangle_size, triangle_1y + triangle_size)
    triangle_3x, triangle_3y = random.randint(triangle_2x - triangle_size,
                                              triangle_2x + triangle_size), random.randint(
        triangle_2y - triangle_size, triangle_2y + triangle_size)
    a = area(triangle_1x, triangle_1y, triangle_2x, triangle_2y, triangle_3x, triangle_3y)
    if a < 7000:
        continue
    else:
        collinear = 1
triangle_surf = pg.Surface((1860, 1150))
while slope == 0:
    a1, a2, a3 = -1 * ((triangle_2y - triangle_1y) / (triangle_2x - triangle_1x)), -1 * (
            (triangle_3y - triangle_2y) / (triangle_3x - triangle_2x)), -1 * (
                         (triangle_1y - triangle_3y) / (triangle_1x - triangle_3x))
    c1, c2, c3 = -1 * (triangle_1y + a1 * triangle_1x), -1 * (triangle_2y + a2 * triangle_2x), -1 * (
            triangle_3y + a3 * triangle_3x)
    if abs(a1) > 4 or abs(a2) > 4 or abs(a3) > 4:
        triangle_1x, triangle_1y = random.randint(450, 1460), random.randint(250, 790)
        triangle_2x, triangle_2y = random.randint(triangle_1x - triangle_size,
                                                  triangle_1x + triangle_size), random.randint(
            triangle_1y - triangle_size, triangle_1y + triangle_size)
        triangle_3x, triangle_3y = random.randint(triangle_2x - triangle_size,
                                                  triangle_2x + triangle_size), random.randint(
            triangle_2y - triangle_size, triangle_2y + triangle_size)
    else:
        slope = 1
        pg.draw.polygon(triangle_surf, "chartreuse4",
                        [(triangle_1x, triangle_1y), (triangle_2x, triangle_2y), (triangle_3x, triangle_3y)])
        pg.draw.lines(triangle_surf, "cornflowerblue", False,
                      [(triangle_1x, triangle_1y), (triangle_2x, triangle_2y), (triangle_3x, triangle_3y),
                       (triangle_1x, triangle_1y)], width=5)
triangle_mask = pg.mask.from_surface(triangle_surf)
# Make sure to set colorkey after mask for proper detection
triangle_surf.set_colorkey((0, 0, 0))
profile_text = pg.font.Font("eurostile.TTF", 25)
profile_text2 = profile_text.render("Profile", True, "black")
text = pg.font.Font("Precious.ttf", 50)
text2 = text.render("Play Game", True, "black")
profile_info = pg.font.Font("eurostile.TTF", 115)
profile_name = profile_info.render("First Name :", True, "black")
profile_last = profile_info.render("Last Name :", True, "black")
profile_date = profile_info.render("Birthdate :", True, "black")
profile_user = profile_info.render("Username :", True, "black")
# login_class.profile_user is used since you can't use login_class.user.get()
profile_name_info = profile_info.render(
    f"{login_class.records_list[login_class.records_list.index(login_class.profile_user) - 3]}", True, "black")
profile_last_info = profile_info.render(
    f"{login_class.records_list[login_class.records_list.index(login_class.profile_user) - 2]}", True, "black")
profile_date_info = profile_info.render(
    f"{login_class.records_list[login_class.records_list.index(login_class.profile_user) - 1]}", True, "black")
profile_user_info = profile_info.render(f"{login_class.profile_user}", True, "black")
playing_class = pg.sprite.GroupSingle(Rotate(music_list["HNNY&KOKO-boy.mp3"]))
pg.mixer.music.load(list(music_list.keys())[0])
pg.mixer.music.play(-1)
stopwatch = Stopwatch(2)
stopwatch.start()
while login_class.access:
    keys = pg.key.get_pressed()
    mouse_x, mouse_y = pg.mouse.get_pos()
    # Update Song
    if stopwatch.duration + increment2 >= list(length_dict.values())[x % 5]:
        pg.mixer.music.fadeout(1000)
        increment, increment2 = 0, 0
        playing_class = pg.sprite.GroupSingle(Rotate(list(music_list.values())[(x + 1) % 5]))
        pg.mixer.music.load(list(music_list.keys())[(x + 1) % 5])
        pg.mixer.music.play(-1)
        stopwatch.restart()
        x += 1
    elif increment2 > increment:
        increment, increment2 = 0, increment2 - increment
    elif increment2 == increment:
        increment, increment2 = 0, 0
    else:
        increment2, increment = 0, increment - increment2
    player_rect.center = pg.mouse.get_pos()
    pauseplay_rect = pg.Rect((ipod_rect[0] + 90, ipod_rect[1] + 280, 20, 20))
    forward_rect = pg.Rect((ipod_rect[0] + 132, ipod_rect[1] + 227, 30, 20))
    backward_rect = pg.Rect((ipod_rect[0] + 37, ipod_rect[1] + 227, 30, 20))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                if pauseplay_rect.collidepoint(event.pos):
                    music_update = not music_update
                elif backward_rect.collidepoint(event.pos):
                    if stopwatch.duration + increment2 <= 10:
                        pg.mixer.music.fadeout(1000)
                        x -= 1
                        increment, increment2 = 0, 0
                        playing_class = pg.sprite.GroupSingle(Rotate(list(music_list.values())[x % 5]))
                        pg.mixer.music.load(list(music_list.keys())[x % 5])
                        pg.mixer.music.play(-1)
                        stopwatch.restart()
                    else:
                        pg.mixer.music.set_pos((stopwatch.duration - increment) - 10)
                        increment += 10
                elif forward_rect.collidepoint(event.pos):
                    pg.mixer.music.set_pos((stopwatch.duration + increment2) + 10)
                    increment2 += 10
                elif ipod_rect.collidepoint(event.pos):
                    rectangle_dragging = True
                    mouse_x, mouse_y = event.pos
                    offset_x = ipod_rect.x - mouse_x
                    offset_y = ipod_rect.y - mouse_y
        elif event.type == pg.MOUSEBUTTONUP:
            if event.button == 1:
                rectangle_dragging = False
        elif event.type == pg.MOUSEMOTION:
            if rectangle_dragging:
                mouse_x, mouse_y = event.pos
                ipod_rect.x = mouse_x + offset_x
                ipod_rect.y = mouse_y + offset_y
    if menu:
        screen.fill("lightsteelblue1")
        pg.draw.rect(screen, "royalblue4", menu_rect, border_radius=50)
        pg.draw.rect(screen, (64, 64, 64), menu_rect, width=5, border_radius=50)
        pg.draw.rect(screen, (255, 255, 255), (35, 2, 80, 30), border_radius=5)
        pg.draw.rect(screen, (0, 0, 0), (35, 2, 80, 30), width=2, border_radius=5)
        screen.blit(profile_text2, (40, 5))
        screen.blit(text2, (790, 550))
        # Blit ipod last to have it be on top of all other images
        screen.blit(ipod, ipod_rect)
        pg.draw.rect(screen, (0, 0, 0), ipod_rect, width=2, border_radius=17)
        pg.draw.rect(screen, (0, 0, 0), (ipod_rect[0] + 17, ipod_rect[1] + 15, 168, 130), border_radius=7)
        if music_update:
            playing_class.update()
            if music_paused:
                stopwatch.start()
                pg.mixer.music.unpause()
                music_paused = not music_paused
        else:
            music_paused = True
            stopwatch.stop()
            pg.mixer.music.pause()
        playing_class.draw(ipod_surf)
        screen.blit(ipod_surf, (ipod_rect[0] + 17, ipod_rect[1] + 15))
        time()
        start_time2 = pg.time.get_ticks()
        if event.type == pg.MOUSEBUTTONDOWN and menu_rect.collidepoint(player_rect.center):
            menu, play = False, True
        if event.type == pg.MOUSEBUTTONDOWN and profile_rect.collidepoint(player_rect.center):
            menu, profile_screen = False, True
    if profile_screen:
        screen.fill("lightsteelblue1")
        pg.draw.line(screen, (0, 0, 0), (0, 25), (1860, 25))
        screen.blit(back, back_rect)
        screen.blit(profile_name, (15, 40))
        screen.blit(profile_last, (15, 270))
        screen.blit(profile_date, (15, 500))
        screen.blit(profile_user, (15, 730))
        screen.blit(profile_name_info, (700, 40))
        screen.blit(profile_last_info, (700, 270))
        screen.blit(profile_date_info, (700, 500))
        screen.blit(profile_user_info, (700, 730))
        screen.blit(ipod, ipod_rect)
        pg.draw.rect(screen, (0, 0, 0), ipod_rect, width=2, border_radius=17)
        pg.draw.rect(screen, (0, 0, 0), (ipod_rect[0] + 17, ipod_rect[1] + 15, 168, 130), border_radius=7)
        if music_update:
            playing_class.update()
            if music_paused:
                pg.mixer.music.unpause()
                stopwatch.start()
                music_paused = not music_paused
        else:
            music_paused = True
            pg.mixer.music.pause()
            stopwatch.stop()
        playing_class.draw(ipod_surf)
        screen.blit(ipod_surf, (ipod_rect[0] + 17, ipod_rect[1] + 15))
        if event.type == pg.MOUSEBUTTONDOWN and back_rect.collidepoint(player_rect.center):
            menu, profile_screen = True, False
    if play:
        start_time = start_time2
        screen.fill((161, 179, 196))
        time()
        # draw on screen
        screen.blit(triangle_surf, (0, 0))
        screen.blit(circle_surf, (0, 0))
        screen.blit(ellipse_surf, (0, 0))
        screen.blit(arc_surf, (0, 0))
        screen.blit(ipod, ipod_rect)
        pg.draw.rect(screen, (0, 0, 0), ipod_rect, width=2, border_radius=17)
        pg.draw.rect(screen, (0, 0, 0), (ipod_rect[0] + 17, ipod_rect[1] + 15, 168, 130), border_radius=7)
        if music_update:
            playing_class.update()
            if music_paused:
                pg.mixer.music.unpause()
                stopwatch.start()
                music_paused = not music_paused
        else:
            music_paused = True
            pg.mixer.music.pause()
            stopwatch.stop()
        playing_class.draw(ipod_surf)
        screen.blit(ipod_surf, (ipod_rect[0] + 17, ipod_rect[1] + 15))
        # check if mouse is on arc
        if arc_mask.overlap(player_mask, (player_rect.left, player_rect.top)):
            pass
        # check if mouse is on circle
        if circle_mask.overlap(player_mask, (player_rect.left, player_rect.top)):
            pass
        # check if mouse is on triangle
        if triangle_mask.overlap(player_mask, (player_rect.left, player_rect.top)):
            pass
        # check if mouse is on ellipse
        if ellipse_mask.overlap(player_mask, (player_rect.left, player_rect.top)):
            pass
    pg.display.update()
    clock.tick(60)
