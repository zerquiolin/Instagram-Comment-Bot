from BotBuilder import BotBuilder
import time

instagramPaths = {
    'usernameField' : '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input',
    'secretField' : '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input',
    'loginButton' : '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button',
    'facebookOption' : '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[5]/button',
    'facebookUsernameField' : '/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/form/div/div[1]/input',
    'facebookSecretField' : '/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/form/div/div[2]/input',
    'facebookLoginButton' : '/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/form/div/div[3]/button'
}
defaultBotConfig = {
    'sleepTimeOnAction' : 5,
    'sleepTimeOnLoad' : 15,
    'facebookSleepTimeOnLoad' : 20,
    'sleepTimeOverPost' : 5,
    'sleepTimeOverSpam' : 600
}

class BotTemplate:

    def __init__(self, bot, botConfig = defaultBotConfig):
        self.bot = bot
        self.botConfig = botConfig
        self.BotBuilder = BotBuilder('chromedriver.exe')
    
    def start(self):
        try:
            self.openPage()
            self.logIn()
            self.goToPost()
            while True:
                self.comment()
                time.sleep(self.botConfig['sleepTimeOverSpam'])
        except:
            print('I died...')

    def openPage(self):
        self.BotBuilder.goTo('https://instagram.com')
        time.sleep(self.botConfig['sleepTimeOnLoad'])

    def logIn(self):
        if self.bot['facebook']:
            self.BotBuilder.clickOn(instagramPaths['facebookOption'])
            time.sleep(self.botConfig['sleepTimeOnLoad'])
            self.BotBuilder.typeOn(instagramPaths['facebookUsernameField'], self.bot['username'])
            time.sleep(self.botConfig['sleepTimeOnAction'])
            self.BotBuilder.typeOn(instagramPaths['facebookSecretField'], self.bot['secret'])
            time.sleep(self.botConfig['sleepTimeOnAction'])
            self.BotBuilder.clickOn(instagramPaths['facebookLoginButton'])
            time.sleep(self.botConfig['facebookSleepTimeOnLoad'])
            return
        
        self.BotBuilder.typeOn(instagramPaths['usernameField'], self.bot['username'])
        time.sleep(self.botConfig['sleepTimeOnAction'])
        self.BotBuilder.typeOn(instagramPaths['secretField'], self.bot['secret'])
        time.sleep(self.botConfig['sleepTimeOnAction'])
        self.BotBuilder.clickOn(instagramPaths['loginButton'])
        time.sleep(self.botConfig['sleepTimeOnLoad'])

    def goToPost(self):
        self.BotBuilder.goTo(self.bot['post'])
        time.sleep(self.botConfig['sleepTimeOnLoad'] + 2)

    def comment(self):
        for index in range(6):
            self.BotBuilder.clickOn(self.bot['commentField'])
            time.sleep(self.botConfig['sleepTimeOnAction'])
            self.BotBuilder.typeOn(self.bot['commentField'], self.bot['comment'])
            time.sleep(self.botConfig['sleepTimeOnAction'])
            self.BotBuilder.clickOn(self.bot['postButton'])
            time.sleep(self.botConfig['sleepTimeOverPost'])