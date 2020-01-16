# -*- coding: utf-8 -*-
import string
import random
import pytest

from model.contact import Contact


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


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contacts_list
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contact = app.contact.get_contacts_list
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
