from sys import maxsize


class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, company=None, address=None,
                 homephone=None, mobilephone=None, workphone=None, fax=None, email=None, id=None,
                 all_phones_from_home_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.fax = fax
        self.email = email
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s:%s" % (
            self.id, self.firstname, self.middlename, self.lastname, self.nickname, self.company, self.address)

    def __eq__(self, other):
        return (
                       self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname, self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
