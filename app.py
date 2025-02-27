import pyquotegen
import telebot
import schedule
import time

chat_id = "replace with chatid [int]" 
bot = telebot.TeleBot("api_key")

def counter():
    with open("data","r") as file:
        days = file.read()
    with open("data","w") as file:
        file.write(str(int(days) - 1))
    return days
def get_quote():
    return pyquotegen.get_quote()
def task():
    bot.send_message(chat_id ,f"{counter()} Days remain from the highschool")
    bot.send_message(chat_id ,f"Today's quote is '*{get_quote()}*'",parse_mode="Markdown")

schedule.every().day.at("10:00").do(task)

while True:
    schedule.run_pending()
    time.sleep(30)
