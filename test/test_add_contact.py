# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(firstname="123", middlename="123", lastname="123", nickname="123", company="123", address="123",
                      home="123", mobile="123", work="123", fax="123", email="123")
    app.contact.create(contact)
    new_contact = app.contact.get_contacts_list()
    assert len(old_contacts) + 1 == len(new_contact)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
