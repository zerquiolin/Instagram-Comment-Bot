# Here there will be just the instance of the bot configuration and the call of the bot template!
from BotTemplate import BotTemplate
from dotenv import load_dotenv
from threading import Thread
import os
import time

load_dotenv()

firstUserConfig = {
    'username': os.getenv('FIRSTUSERNAME'), 
    'secret': os.getenv('FIRSTSECRET'), 
    'post' : 'https://www.instagram.com/p/CWrpE0mICFR/',
    'comment' : 'Amazing!',
    'commentField' : '/html/body/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/textarea', 
    'postButton' : '/html/body/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/button[2]',
    'facebook': True
}
secondUserConfig = {
    'username': os.getenv('SECONDUSERNAME'), 
    'secret': os.getenv('SECONDSECRET'), 
    'post' : 'https://www.instagram.com/p/CWrpE0mICFR/',
    'comment' : 'Amazing!',
    'commentField' : '/html/body/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/textarea', 
    'postButton' : '/html/body/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/button[2]',
    'facebook': False
}
thirdUserConfig = {
    'username': os.getenv('THIRDUSERNAME'), 
    'secret': os.getenv('THIRDSECRET'), 
    'post' : 'https://www.instagram.com/p/CWrpE0mICFR/',
    'comment' : 'Amazing!',
    'commentField' : '/html/body/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/textarea', 
    'postButton' : '/html/body/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/button[2]',
    'facebook': False
}
botConfig = {
    'sleepTimeOnAction' : 1,
    'sleepTimeOnLoad' : 5,
    'facebookSleepTimeOnLoad' : 10,
    'sleepTimeOverPost' : 2,
    'sleepTimeOverSpam' : 600
}
# If looking to use more than 3 accounts, create a new userConfig and add it to the users list.
users = [firstUserConfig, secondUserConfig, thirdUserConfig]
threads = []

def startBot(userConfig, botConfig):
    firstBot = BotTemplate(userConfig, botConfig)
    firstBot.start()

for user in users:
    thread = Thread(target=startBot, args=[user, botConfig])
    threads.append(thread)

for thread in threads:
    thread.start()
