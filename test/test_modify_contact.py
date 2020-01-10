from model.contact import Contact


def test_modify_first_contact(app):
    app.contact.modify_first_contact(
        Contact(firstname="333", middlename="333"))
