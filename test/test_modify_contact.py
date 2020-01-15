from random import randrange

from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count == 0:
        app.group.create(Contact(firstname="test"))
    contact = Contact(firstname="Test")
    old_contacts = app.contact.get_contacts_list
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index)
    new_contacts = app.contact.get_contacts_list
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

