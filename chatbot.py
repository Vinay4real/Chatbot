from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot=ChatBot('Marupilla')
bot.set_trainer(ListTrainer)

while True:
    message=input('Vinay Teja:')
    if message.strip()!='Bye':
        reply=bot.get_response(message)
        print('Marupilla:',reply)
    if message.strip()=='Bye':
        print('Marupilla: Bye')
        break
