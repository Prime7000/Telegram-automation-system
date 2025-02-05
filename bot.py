# getting data from server database

import sqlite3

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# sending images
import requests
import datetime
import pytz
import time as prime_time

def task(img,message,bot_key):
    if img != 'products/pngwing.com_17.png':
        print('-------------------Image Available-------------------')
        key = bot_key
        base_url = f"https://api.telegram.org/{key}/SendPhoto"
        caption = message
        image = img
        img = f"media/{image}"

        parameter = {
            "chat_id": '-4684228716',
            "caption": caption
        }

        with open(img, "rb") as image_file:
            res = requests.post(base_url, data=parameter, files={"photo": image_file})

        print(res.text)
    else:
        print('-------------------No Image-------------------')
        key = bot_key
        base_url = f"https://api.telegram.org/{key}/SendMessage"

        parameter = {
            "chat_id": '-4684228716',
            'text': message
        }

        res = requests.get(base_url, parameter)
        print(res.text)

while True:
    cursor.execute('SELECT * FROM core_test')
    for row in cursor.fetchall():
        id = row[0]
        img = row[1]
        message = row[2]
        repeat = row[3]
        robot_id = row[4]
        time = row[5]
        timeframe = row[6]

        # Fetch the bot key from core_robot using robot_id
        cursor.execute('SELECT robot_key FROM core_robot WHERE id = ?', (robot_id,))
        bot_key_result = cursor.fetchone()
        
        if bot_key_result:
            bot_key = bot_key_result[0]  # Extract the key from the result
            # print(bot_key)

        wat_timezone = pytz.timezone('Africa/Lagos')
        now_wat = datetime.datetime.now(wat_timezone)

        if repeat == 1:
            if timeframe == 'daily':
                t = time.split(" ")
                set_time = t[1]
                # print(set_time)
                now_time = str(now_wat.strftime('%H:%M:%S'))
                # print(now_time)
                # print('current time', now_time)
                # print('set time', set_time)

                if now_time == set_time:
                    task(img,message,bot_key)
                    print('daily executed')
                    

            elif timeframe == 'weekly':
                t = time.split(" ")
                set_date = t[0].split('-')
                set_time = t[1]
                year, month, day = set_date

                # print(set_date)
                # print(set_time)
                # print(year,month,day)

                date_obj = datetime.date(int(year),int(month),int(day))
                day_name = date_obj.strftime("%A")
                now_time = now_wat.strftime('%H:%M:%S')
                # print(day_name)

                current_day = now_wat.strftime('%A')

                if current_day == day_name and set_time == now_time:
                    task(img,message,bot_key)
                    print('weekly executed')


            elif timeframe == 'monthly':
                t = time.split(" ")
                set_date = t[0].split('-')
                set_time = t[1]
                year, month, day = set_date

                # print(set_date)
                # print(set_time)
                # print(year,month,day)

                date_obj = datetime.date(int(year),int(month),int(day))
                day_name = date_obj.strftime("%A")
                now_time = now_wat.strftime('%H:%M:%S')
                # print(day_name)

                current_day = now_wat.strftime('%A')
                current_month = now_wat.strftime('%m').strip()
                set_month = month.strip()

                if current_day == day_name and set_time == now_time and current_month == set_month:
                    task(img,message,bot_key)
                    print('monthly executed')

                
            elif timeframe == 'yearly':
                t = time.split(" ")
                set_date = t[0].split('-')
                set_time = t[1]
                year, month, day = set_date

                # print(set_date)
                # print(set_time)
                # print(year,month,day)

                date_obj = datetime.date(int(year),int(month),int(day))
                day_name = date_obj.strftime("%A")
                now_time = now_wat.strftime('%H:%M:%S')
                # print(day_name)

                current_day = now_wat.strftime('%A')
                current_month = now_wat.strftime('%m').strip()
                set_month = month.strip()
                current_year = now_wat.strftime('%Y').strip()
                set_year = year.strip()

                if current_day == day_name and set_time == now_time and current_month == set_month and current_year == set_year:
                    task(img,message,bot_key)
                    print('yearly executed')

            
        else:
            # print('--------------no repeat----------------')
            t = time.split(" ")
            set_date = t[0].strip()
            set_time = t[1].strip()


            current_date = now_wat.strftime('%Y-%m-%d').strip()
            current_time = now_wat.strftime('%H:%M:%S').strip()


            # print('---------------------------------------------')
            # print('set_time', set_time)
            # print('current_time',current_time)
            # print('-------------------------')
            # print('set_date', set_date)
            # print('current_date',current_date)

            if set_date == current_date and set_time == current_time:
                task(img,message,bot_key)
                print('no repeat executed')

    prime_time.sleep(1)


conn.close()