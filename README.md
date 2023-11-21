# Warp Cloudflare 1.1.1.1 GUI

A GUI application based on [warp-cli](https://developers.cloudflare.com/warp-client/get-started/linux) for Linux.

## Installation

Read the [warp-cli install](https://developers.cloudflare.com/warp-client/get-started/linux) documentation. Install `warp-cli` and
register with the `$ warp-cli register` command.

> 👉 Make Sure to create Virtual Environment

Then execute the following commands:

    $ git clone https://github.com/anakin-dabir/1.1.1.1
    $ cd 1.1.1.1
    $ python3 install.py
    $ pyinstaller --onefile --add-data "~/1.1.1.1/icons:icons" main.py
    $ sudo chmod +x ~/.local/share/applications/1.1.1.1.desktop

Now search for `1.1.1.1` in your desktop menu.

> 👉 After the installation please make sure you do not remove 1.1.1.1/dist/ directory

## Uninstall

Remove the `~/.local/share/applications/1.1.1.1.desktop` file.
