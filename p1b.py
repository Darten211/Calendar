import pygame as pg
import p2b as part2
import textwrapping
import datetime as dt
import keyboard_input as ki

pg.init()
part2.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BEIGE = (201, 166, 125)

PINK_PALETTE = [(212, 119, 145), (227, 161, 180), (237, 185, 206)]
GREEN_PALETTE = [(106, 194, 168), (160, 232, 211), (192, 237, 224)]
VIOLET_PALETTE = [(165, 132, 199), (198, 175, 222), (208, 193, 224)]
ORANGE_PALETTE = [(227, 188, 137), (246, 218, 184), (230, 217, 195)]

WIDTH = 1280
HEIGHT = 720
SIZE = (WIDTH, HEIGHT)
TITLE = 'Planner'
YEAR = 2020
NO_ROWS = 200
INTERLINE = 0.9

#part2.create_database(YEAR, NO_ROWS)

habit_font = pg.font.SysFont('segoeprint', 20)
day_font = pg.font.SysFont('segoeprint', 35)
weekday_font = pg.font.SysFont('gabriola', 35)
month_font = pg.font.SysFont('segoeprint', 55)
symbol_font = pg.font.SysFont('arial', 44)

display = pg.display.set_mode(SIZE)
pg.display.set_caption(TITLE)

run = True
clock = pg.time.Clock()

COLOR_PALETTE = PINK_PALETTE

bg_color =  COLOR_PALETTE[1]

current_string = ''
input_mode = False
input_date = dt.date(1, 1, 1)
input_box_surf = day_font.render('', True, WHITE)

class Button:

    X = 0
    Y = 0
    SIZE_X = 30
    SIZE_Y = 30
    BORDER_COLOR = (0, 0, 0)
    BORDER_THICKNESS = 1
    BUTTON_DATE = (1, 1, 1)

    def __init__(self, X, Y, color, thickness, date):
        self.X = X
        self.Y = Y
        self.BORDER_COLOR = color
        self.BORDER_THICKNESS = thickness
        self.BUTTON_DATE = date

    def draw_button(self):
        pg.draw.rect(display, WHITE, [self.X, self.Y, self.SIZE_X, self.SIZE_Y], 0)
        pg.draw.rect(display, self.BORDER_COLOR, [self.X, self.Y, self.SIZE_X, self.SIZE_Y], self.BORDER_THICKNESS)
        plus_surface = symbol_font.render('+', True, (self.BORDER_COLOR))
        display.blit(plus_surface, (self.X + 5, self.Y - 13))

    def is_clicked(self):
        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()

        if self.X < mouse[0] < self.X + self.SIZE_X and self.Y < mouse[1] < self.Y + self.SIZE_Y:
            if click[0] == 1:
                global input_mode, input_date
                input_mode = True
                input_date = self.BUTTON_DATE

class Block:

    X = 0
    Y = 0
    SIZE_X = 260
    SIZE_Y = 550
    BORDER_COLOR = (0, 0, 0)
    BORDER_THICKNESS = 1
    BLOCK_DATE = dt.date(1, 1, 1)

    is_visible = False
    position = -1
    habit_list = []
    add_button = Button(X + 10, Y + 200, BORDER_COLOR, 2, BLOCK_DATE)

    def __init__(self, X, Y, color, thickness, number):
        self.X = X
        self.Y = Y
        self.BORDER_COLOR = color
        self.BORDER_THICKNESS = thickness
        self.habit_list = part2.habits_to_list()
        self.BLOCK_DATE = dt.date(YEAR, 1, 1) + dt.timedelta(days = number)
        self.add_button = Button(self.X + 20, self.Y + 500, self.BORDER_COLOR, 2, self.BLOCK_DATE)

    def write_weekday(self):

        weekday = self.BLOCK_DATE.weekday()
        weekday_string = ''

        if weekday == 0:
            weekday_string = 'Poniedziałek'
        elif weekday == 1:
            weekday_string = 'Wtorek'
        elif weekday == 2:
            weekday_string = 'Środa'
        elif weekday == 3:
            weekday_string = 'Czwartek'
        elif weekday == 4:
            weekday_string = 'Piątek'
        elif weekday == 5:
            weekday_string = 'Sobota'
        elif weekday == 6:
            weekday_string = 'Niedziela'

        weekday_surf = weekday_font.render(weekday_string, True, COLOR_PALETTE[2])

        surf_X = self.X + 140
        if self.BLOCK_DATE.day > 9:
            surf_X += 20
        display.blit(weekday_surf, (surf_X - weekday_surf.get_size()[0] // 2, self.Y + 64 - weekday_surf.get_size()[1]))

    def draw_block(self):
        if self.is_visible:
            pg.draw.rect(display, WHITE, [self.X, self.Y, self.SIZE_X, self.SIZE_Y], 0)
            pg.draw.rect(display, self.BORDER_COLOR, [self.X, self.Y, self.SIZE_X, self.SIZE_Y], self.BORDER_THICKNESS)

            no_line = 0
            for habit in self.habit_list:
                lines = textwrapping.blit_text(display, habit, (self.X + 50, self.Y + 100 + (habit_font.size('A')[1]) * INTERLINE * no_line), habit_font, BEIGE, 220, self.X, INTERLINE)
                no_line += lines

            day_surface = day_font.render(str(self.BLOCK_DATE.day), True, COLOR_PALETTE[0])
            display.blit(day_surface, (self.X + 25, self.Y + 10))
            self.write_weekday()
            self.add_button.draw_button()
            self.add_button.is_clicked()

def set_palette(number):
    if number % 4 == 0:
        return GREEN_PALETTE
    elif number % 4 == 1:
        return PINK_PALETTE
    elif number % 4 == 2:
        return ORANGE_PALETTE
    elif number % 4 == 3:
        return VIOLET_PALETTE

block_list = []
palette_list = []
for n in range(0,NO_ROWS):
    block_sublist = []
    for i in range(0,4):
        block = Block(66 + i*296, 106, set_palette(n)[2], 4, 4 * n + i)
        block.position = i
        block_sublist.append(block)
    block_list.append(block_sublist)
    palette_list.append(set_palette(n))

interval = int((dt.date.today() - dt.date(YEAR, 1, 1)) / dt.timedelta(days = 1))
no_visible = interval // 4
STARTING_VISIBLE = no_visible

for block in block_list[no_visible]:
    block.is_visible = True

def write_month(month):
    
    month_string = ''
    if month == 1:
        month_string = 'Styczeń'
    elif month == 2:
        month_string = 'Luty'
    elif month == 3:
        month_string = 'Marzec'
    elif month == 4:
        month_string = 'Kwiecień'
    elif month == 5:
        month_string = 'Maj'
    elif month == 6:
        month_string = 'Czerwiec'
    elif month == 7:
        month_string = 'Lipiec'
    elif month == 8:
        month_string = 'Sierpień'
    elif month == 9:
        month_string = 'Wrzesień'
    elif month == 10:
        month_string = 'Październik'
    elif month == 11:
        month_string = 'Listopad'
    elif month == 12:
        month_string = 'Grudzień'

    month_surf = month_font.render((month_string.upper() + ' ' + str(block_list[no_visible][0].BLOCK_DATE.year)), True, COLOR_PALETTE[0])
    month_width = month_surf.get_size()[0]
    display.blit(month_surf,(640 - month_width // 2, 5))

shift = False
alt = False
pg.key.set_repeat(500, 50)

while run:

    all_keys = pg.key.get_pressed()
    if all_keys[pg.K_LSHIFT] or all_keys[pg.K_RSHIFT]:
        shift = True
    else:
        shift = False
    
    if all_keys[pg.K_RALT]:
        alt = True
    else:
        alt = False

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            key = event.key
            if key == pg.K_RIGHT:
                if no_visible < NO_ROWS - 1:
                    for block in block_list[no_visible + 1]:
                        block.is_visible = True
                    for block in block_list[no_visible]:
                        block.is_visible = False
                    no_visible += 1
            if key == pg.K_LEFT:
                if no_visible > 0:
                    for block in block_list[no_visible - 1]:
                        block.is_visible = True
                    for block in block_list[no_visible]:
                        block.is_visible = False
                    no_visible -= 1
            if key == pg.K_ESCAPE:
                for block in block_list[no_visible]:
                    block.is_visible = False
                no_visible = STARTING_VISIBLE
                for block in block_list[no_visible]:
                    block.is_visible = True
            if input_mode:
                if key == pg.K_RETURN:
                    part2.add_to_database(YEAR, NO_ROWS, input_date, current_string)
                    current_string = ""
                    input_mode = False
                else:
                    current_string = ki.key_handle(key, current_string, alt, shift)
                    input_box_surf = day_font.render(current_string, True, WHITE)

    display.fill(WHITE)
    COLOR_PALETTE = palette_list[no_visible]

    bg_color = COLOR_PALETTE[1]
    pg.draw.rect(display, bg_color, [30, 0, 1220, 690], 0)

    if input_mode:
        input_width = input_box_surf.get_size()[0]
        if current_string:
            display.blit(input_box_surf, (640 - input_width // 2, 100))
    else:
        for block_sublist in block_list:
            for block in block_sublist:
                block.draw_block()
        write_month(block_list[no_visible][0].BLOCK_DATE.month)

    pg.display.update()
    clock.tick(30)
    
pg.quit()
quit()