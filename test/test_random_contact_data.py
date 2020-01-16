import re
from random import randrange

from model.contact import Contact


def clear(s):
    return re.sub("[() -]", "", s)


def test_all_data_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(firstname="test", lastname="lastname", homephone="123",
                    mobilephone="456", workphone="789", address="address"))
    all_contacts = app.contact.get_contact_list()
    index = randrange(len(all_contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_phones_form_homepage == merge_phones_like_on_homepage(contact_from_edit_page)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address


def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None,
                                                                              [contact.homephone, contact.mobilephone,
                                                                               contact.workphone]))))


