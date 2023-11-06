import telepot

class Telegram():
    def __init__(self):
        my_token = "6723010335:AAHcgR1yxO9vN81w7fTNLEDR5d_e_erf1kg"  # 봇파더에서 얻은 토큰값을 입력합니다.
        self.bot = telepot.Bot(token=my_token)

    def sendMessage(self, message):
        self.bot.sendMessage("-1002139570965", message)

    def getUpdates(self):
        return self.bot.getUpdates()


if __name__ == '__main__':
    bot = Telegram()
    msg = "테스트메시지"
    print(bot.getUpdates())  # 내 ID 확인하는 방법
    bot.sendMessage(msg)
