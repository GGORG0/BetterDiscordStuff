# GnomeBadge
This is a plugin that (hopefully) fixes the annoying Linux Discord unread messages badge. It features a server (the Discord plugin) and a client (a Python script).
You first have to add the plugin, making sure that the 6968 port is free and then run the `badge-updater.py` script in the background.
It can be done like this:
```bash
python3 badge-updater.py &
disown
```
or by using a program like GNU Screen (`screen python3 badge-updater.py` and then close the terminal).
You have to have the [libunity](https://aur.archlinux.org/packages/libunity/) and [PyGObject](https://pygobject.readthedocs.io/en/latest/) libraries installed for this to work.
The script is based on an example in the [Ubuntu/Unity docs](https://wiki.ubuntu.com/Unity/LauncherAPI#Python_Example).

**Note:** If you use Discord Canary, Discord PTB, Powercord, etc. then you'll have to update the `DESKTOP_FILE` variable in the Python script (soon moving to plugin settings).