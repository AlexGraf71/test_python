# -*- coding: utf-8 -*-
import pytest

from data.add_contact import testdata
from model.contact import Contact


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contacts_list
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contact = app.contact.get_contacts_list
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
