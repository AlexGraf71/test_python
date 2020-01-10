class ContactHelper:

    def __init__(self, app):
        self.app = app

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)

    def create(self, contact):
        wd = self.app.wd
        wd.find_element_by_xpath("/html/body/div/div[3]/ul/li[2]/a").click()
        self.fill_contact_form(contact)
        wd.find_element_by_name("submit").click()
        self.app.return_home()

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.return_home()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("/html/body/div[1]/div[4]/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()

    def modify_first_contact(self, contact):
        wd = self.app.wd
        self.app.return_home()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("/html/body/div[1]/div[4]/form[2]/table/tbody/tr[2]/td[8]/a/img").click()
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()
        self.app.return_home()

    def count(self):
        wd = self.app.wd
        self.app.return_home()
        return len(wd.find_element_by_name("selected[]"))

