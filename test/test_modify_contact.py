from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count == 0:
        app.group.create(Contact(firstname="test"))
    app.contact.modify_first_contact(
        Contact(firstname="333", middlename="333"))
