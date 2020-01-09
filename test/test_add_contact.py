# -*- coding: utf-8 -*-
from model.contact import Contact
from fixture.application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="123", middlename="123", lastname="123",
                               nickname="123", company="123", address="123",
                               home="123", mobile="123", work="123", fax="123",
                               email="123"))
    app.session.logout()
