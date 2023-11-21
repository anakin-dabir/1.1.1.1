from warp_gui.mainwindow import GUI
import sys
import warp_gui.errors
import socket

try:
    # check program already running or not
    s = socket.socket()
    s.bind(('', 45367))
except:
    warp_gui.errors.already_running()
    sys.exit(-1)

gui = GUI()
gui.show(hide=True)

