#!/usr/bin/python3

import datetime

def today_date(date):
  return f'{date.day}th {date.month}, {date.year}'


print(today_date(datetime.datetime.today()))
