from model.contact import Contact
import string
import random
import pytest


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_digits(maxlen):
    symbols = string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname=firstname, middlename=middlename, lastname=lastname, nickname=nickname, company=company,
                    address=address, homephone=homephone, mobilephone=mobilephone, workphone=workphone, fax=fax)
            for firstname in ["", random_string("firstname", 10)]
            for middlename in["", random_string("middlename", 10)]
            for lastname in ["", random_string("lastname", 10)]
            for nickname in["", random_string("nickname", 10)]
            for company in ["", random_string("company", 10)]
            for address in["", random_string("address", 10)]
            for homephone in [random_digits(10)]
            for mobilephone in [random_digits(10)]
            for workphone in [random_digits(10)]
            for fax in [random_digits(10)]

]