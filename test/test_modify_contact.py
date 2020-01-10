from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(
        Contact(firstname="333", middlename="333", lastname="121", nickname="123", company="123", address="123",
                home="123", mobile="123", work="123", fax="123", email="123"))
    app.session.logout()
