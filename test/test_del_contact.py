# -*- coding: utf-8 -*-
from random import randrange

from model.contact import Contact


def test_delete_contact(app):
    if app.contact.count == 0:
        app.group.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contacts_list
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contacts_list
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_delete_some_contact(app):
    if app.contact.count == 0:
        app.group.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contacts_list
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    new_contacts = app.contact.get_contacts_list
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[index:index+1] = []
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)