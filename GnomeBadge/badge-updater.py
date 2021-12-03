#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gi.repository import Unity, Gio, GObject, GLib, Dbusmenu
import requests

DESKTOP_FILE = "powercord.desktop"
UPDATE_SECONDS = 2

loop = GLib.MainLoop()

launcher = Unity.LauncherEntry.get_for_desktop_id(DESKTOP_FILE)


# TODO:
#  ql = Dbusmenu.Menuitem.new ()
#  item1 = Dbusmenu.Menuitem.new ()
#  item1.property_set (Dbusmenu.MENUITEM_PROP_LABEL, "Mark as read")
#  item1.property_set_bool (Dbusmenu.MENUITEM_PROP_VISIBLE, True)
#  ql.child_append (item1)
#  launcher.set_property("quicklist", ql)


launcher.set_property("count_visible", True)

prev_pings = 0

def update_pings():
    global prev_pings
    try:
        pings = int(requests.get("http://127.0.0.1:6968/getpings").content.decode())
    except requests.exceptions.ConnectionError:
        pings = 0

    launcher.set_property("count", pings)

    if pings > prev_pings:
        launcher.set_property("urgent", True)
    elif launcher.get_property("urgent"):
        launcher.set_property("urgent", False)


    prev_pings = pings
    return True

GLib.timeout_add_seconds(UPDATE_SECONDS, update_pings)

loop.run()

