import os
import io
import pandas as pd
import datetime as dt

def init():
    try:
        f = open('habits.txt', 'r')
        f.close()
    except:
        f = open('habits.txt', 'x')
        f.close()

def add_habit(habit):
    f_write = io.open('habits.txt', mode = 'a', encoding = 'utf-8')

    if os.stat('habits.txt').st_size == 0:
        f_write.write(habit)
    else:
        f_write.write(',' + habit)

def clear_habits():
    f_clear = open('habits.txt', 'w')
    f_clear.close()

def habits_to_list():
    f_read = io.open('habits.txt', mode = 'r', encoding = 'utf-8')
    list_of_habits = (f_read.read()).split(',')
    return list_of_habits

def create_database(year, no_rows):
    
    COLUMN_NAMES = ['Day', 'Events', 'Tasks', 'TaskStatus', 'HabitStatus']
    export_dict = {}

    for name in COLUMN_NAMES:
        export_dict[name] = []

    startDate = dt.date(year, 1, 1)

    for _ in range(0, 4 * no_rows):
        export_dict['Day'].append(startDate.isoformat())
        export_dict['Events'].append('')
        export_dict['Tasks'].append('')
        export_dict['TaskStatus'].append('')
        export_dict['HabitStatus'].append('')
        startDate += dt.timedelta(days = 1)

    df = pd.DataFrame(export_dict)
    df.to_csv('task_database.csv', sep = ';', index = False)

def add_to_database(year, no_rows, target_date, target_string):
    
    df = pd.read_csv('task_database.csv', delimiter = ';')
    list_of_rows = [list(row) for row in df.values]

    pos = int((target_date - dt.date(year, 1, 1)) / dt.timedelta(days = 1))
    if list_of_rows[pos][2]:
        list_of_rows[pos][2] = target_string
    else:
        list_of_rows[pos][2] = str(list_of_rows[pos][2]) + ',' + target_string
    
    COLUMN_NAMES = ['Day', 'Events', 'Tasks', 'TaskStatus', 'HabitStatus']
    export_dict = {}

    for name in COLUMN_NAMES:
        export_dict[name] = []

    for i in range(0, 4 * no_rows):
        export_dict['Day'].append(list_of_rows[i][0])
        export_dict['Events'].append(list_of_rows[i][1])
        export_dict['Tasks'].append(list_of_rows[i][2])
        export_dict['TaskStatus'].append(list_of_rows[i][3])
        export_dict['HabitStatus'].append(list_of_rows[i][4])

    df = pd.DataFrame(export_dict)
    df.to_csv('task_database.csv', sep = ';', index = False)