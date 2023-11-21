import os
import sys
from pathlib import Path

cur_path = sys.path[0]

os.system("pip3 install -U pip wheel setuptools")
os.system("pip3 install -r requirements.txt")
os.system('echo "export HOME={}" >> ~/.bashrc'.format(cur_path))
os.system("cp {}/icons/logo.png ~/.local/share/icons/warp_gui.png".format(cur_path))

desktop_file = '{}/.local/share/applications/1.1.1.1.desktop'.format(Path.home())

file = open(desktop_file, 'w+')
file.write('''[Desktop Entry]
Name=1.1.1.1 
Version=1.0
Comment=GUI based App for WARP Cloudflare 1.1.1.1 VPN
Exec=$HOME/1.1.1.1/dist/main
Icon=warp_gui
Terminal=false
Type=Application
Comment[en_US.UTF-8]=GUI based App for WARP Cloudflare 1.1.1.1 VPN
'''.format(cur_path))
print('Desktop file created at "{}"'.format(desktop_file))


