import pyquotegen
import telebot
import schedule
import time

bot = telebot.TeleBot("6981201641:AAHEfBoXqx-DtuS9xr6v6QiheXyfUYLPDbk")

def counter():
    with open("data","r") as file:
        days = file.read()
    with open("data","w") as file:
        file.write(str(int(days) - 1))
    return days
def get_quote():
    return pyquotegen.get_quote()
def task():
    bot.send_message(-1002017941746,f"{counter()} Days remain from the highschool")
    bot.send_message(-1002017941746,f"Today's quote is '*{get_quote()}*'",parse_mode="Markdown")

schedule.every().day.at("10:00").do(task)

while True:
    schedule.run_pending()
    time.sleep(30)
