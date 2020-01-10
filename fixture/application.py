from selenium import webdriver

from fixture.contact import ContactHelper
from fixture.group import GroupHelper
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def return_home(self):
        wd = self.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_xpath("/html/body/div[1]/div["
                                                                                           "4]/form["
                                                                                           "2]/table/tbody/tr[1]/th["
                                                                                           "2]/a")) > 0):
            wd.find_element_by_xpath("/html/body/div[1]/div[3]/ul/li[1]/a").click()

    def destroy(self):
        self.wd.quit()
