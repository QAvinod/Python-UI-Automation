from testCases import Login
from PageObjects import MenuPage


class MassInterviewFlow:
    def __init__(self):
        Login1 = Login.Login()
        Login1.crpo_login()

    def test(self):
        print('vinod')
        MenuPage.event(self)


Object = MassInterviewFlow()
Object.test()
