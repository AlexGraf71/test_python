# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="zaq1"))


def test_modify_group_header(app):
    app.group.modify_first_group(Group(nheader="xsw2"))
