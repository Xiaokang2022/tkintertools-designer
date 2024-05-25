import tkintertools as tkt
import tkintertools.style as style

from . import windows

root = tkt.Tk(title="Login")
root.center()
login = windows.LoginToplevel(
    root, (480, 640), title="登录", transient=True, grab=True)
login.resizable(False, False)
login._theme(style.DARK_MODE)
login.center()
login.load_ui()
