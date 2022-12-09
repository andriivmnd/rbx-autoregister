import random
import string
from time import sleep

import requests
import xlsxwriter
from datetime import datetime

# Settings
nickname_size = 8
password_size = 30
row = 0

def gennick():
    nickname = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(nickname_size))
    nickname+= str(random.randint(1, 1000))
    request = requests.get('https://api.roblox.com/users/get-by-username?username=' + nickname)
    if request.status_code == 200:
        if "Id" in request.json():
            print("Nickname exist.. Retrying")
            gennick()
    elif request.status_code == 429:
        sleep(1)
    return nickname

def generate():
    nickname = gennick()
    while True:
        password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(password_size))
        if (sum(c.islower() for c in password) >= 4
                and sum(c.isupper() for c in password) >= 4
                and sum(c.isdigit() for c in password) >= 4):
            break
    pincode = str(random.randint(1111, 9999))
    return nickname, password, pincode


def create(name):
    excel_book = xlsxwriter.Workbook(name)
    worksheet = excel_book.add_worksheet(datetime.now().strftime("%d.%m.%y|%H.%M.%S"))

    row = 0
    print("Enter count: ")
    count = int(input())
    print(f"Generating {count} nicks")
    for i in range(count):
        nick, password, pincode = generate()
        worksheet.write(row, 0, nick)
        worksheet.write(row, 1, password)
        worksheet.write(row, 3, pincode)
        print(nick + "  " + password + "   " + pincode)
        row+=1
    excel_book.close()
