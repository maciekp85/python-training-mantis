from selenium import webdriver

from fixture.james import JamesHelper
from fixture.session import SessionHelper
from fixture.signup import SignupHelper
from fixture.mail import MailHelper


class Application:

    def __init__(self, browser, config):
        if browser == "firefox":
            self.wd = webdriver.Firefox(capabilities={"marionette": False},
                                firefox_binary="C:/Program Files (x86)/Mozilla Firefox/ESR/firefox.exe")
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognised browser %s" % browser)
        self.session = SessionHelper(self)
        self.james = JamesHelper(self)
        self.signup = SignupHelper(self)
        self.mail = MailHelper(self)
        self.config = config
        self.base_url = config['web']['baseUrl']

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()
