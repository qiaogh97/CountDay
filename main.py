import os
import datetime

from zhdate import ZhDate
from config_private import *

def check_year_solar(item):
    today = datetime.date.today()
    year, month, day, calender, date_type, description = item
    if int(month)==today.month and int(day)==today.day:
        if year is None:
            print(f'今天是{description}:{today.month}月{today.day}号.')
        else:
            print(f'今天是{description}:{year}年{today.month}月{today.day}号, {today.year-int(year)}年.')

def check_year_lunar(item):
    year, month, day, calender, date_type, description = item
    today = datetime.date.today()
    try:
        goal_date = ZhDate(today.year, int(month), int(day)).to_datetime().date()
    except TypeError:
        return
    if (goal_date-today).days==0:
        if year is None:
            print(f'今天是{description}:{month}月{day}号.')
        else:
            print(f'今天是{description}:{year}年{month}月{day}号, {today.year-int(year)}年.')

def check_number_solar(item, day_num):
    year, month, day, calender, date_type, description = item
    if year is None:
        return
    goal_date = datetime.date(int(year), int(month), int(day))
    today = datetime.date.today()
    delta = today - goal_date
    if delta.days==day_num:
        print(f'今天是{description}{day_num}天')

def check_number_lunar(item, day_num):
    year, month, day, calender, date_type, description = item
    if year is None:
        return
    today = datetime.date.today()
    goal_date = ZhDate(int(year), int(month), int(day)).to_datetime().date()
    if (today-goal_date).days==day_num:
        print(f'今天是{description}:距离{year}年{month}月{day}号已经{day_num}天了.')

def main():
    for item in data_list:
        year, month, day, calender, date_type, description = item
        if calender == 'solar':
            check_year_solar(item)
            check_number_solar(item, 100)
            check_number_solar(item, 520)
            check_number_solar(item, 1000)
            check_number_solar(item, 1314)
            check_number_solar(item, 10000)
        elif calender == 'lunar':
            check_year_lunar(item)
            check_number_lunar(item, 100)
            check_number_lunar(item, 520)
            check_number_lunar(item, 1000)
            check_number_lunar(item, 1314)
            check_number_lunar(item, 10000)
        else:
            raise Exception(f'calender type must be [solar, lunar], but get "{calender}".')


if __name__=='__main__':
    main()
    print(f'Done.')
